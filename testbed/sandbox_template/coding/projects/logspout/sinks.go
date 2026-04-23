package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"strings"
)

type Sink interface {
	Write(entry map[string]any) error
}

func NewSink(spec string) (Sink, error) {
	parts := strings.SplitN(spec, ":", 2)
	kind := parts[0]

	switch kind {
	case "stdout":
		return &StdoutSink{}, nil
	case "file":
		if len(parts) != 2 {
			return nil, fmt.Errorf("file sink requires path: file:path.log")
		}
		f, err := os.OpenFile(parts[1], os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
		if err != nil {
			return nil, err
		}
		return &FileSink{f: f}, nil
	case "webhook":
		if len(parts) != 2 {
			return nil, fmt.Errorf("webhook sink requires url: webhook:https://example.com/hook")
		}
		return &HTTPSink{url: parts[1]}, nil
	default:
		return nil, fmt.Errorf("unknown sink kind: %q", kind)
	}
}

type StdoutSink struct{}

func (s *StdoutSink) Write(entry map[string]any) error {
	return json.NewEncoder(os.Stdout).Encode(entry)
}

type FileSink struct {
	f *os.File
}

func (s *FileSink) Write(entry map[string]any) error {
	return json.NewEncoder(s.f).Encode(entry)
}

type HTTPSink struct {
	url string
}

func (s *HTTPSink) Write(entry map[string]any) error {
	body, err := json.Marshal(entry)
	if err != nil {
		return err
	}
	resp, err := http.Post(s.url, "application/json", bytes.NewReader(body))
	if err != nil {
		return err
	}
	defer resp.Body.Close()
	if resp.StatusCode >= 400 {
		return fmt.Errorf("webhook returned status %d", resp.StatusCode)
	}
	return nil
}
