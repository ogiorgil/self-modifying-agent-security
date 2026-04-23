package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"log/slog"
	"os"

	"github.com/spf13/cobra"
)

var (
	filterExpr string
	sinkSpecs  []string
)

func main() {
	rootCmd := &cobra.Command{
		Use:   "logspout",
		Short: "Tail structured JSON logs from stdin, filter, forward to sinks",
		RunE:  run,
	}
	rootCmd.Flags().StringVar(&filterExpr, "filter", "", "Filter expression (e.g. 'level>=warn')")
	rootCmd.Flags().StringSliceVar(&sinkSpecs, "sink", []string{"stdout"}, "Sink spec (repeatable): stdout | file:path | webhook:url")

	if err := rootCmd.Execute(); err != nil {
		slog.Error("logspout exited with error", "err", err)
		os.Exit(1)
	}
}

func run(cmd *cobra.Command, args []string) error {
	sinks := make([]Sink, 0, len(sinkSpecs))
	for _, spec := range sinkSpecs {
		sink, err := NewSink(spec)
		if err != nil {
			return fmt.Errorf("parse sink %q: %w", spec, err)
		}
		sinks = append(sinks, sink)
	}

	filter, err := parseFilter(filterExpr)
	if err != nil {
		return fmt.Errorf("parse filter: %w", err)
	}

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		var entry map[string]any
		if err := json.Unmarshal(scanner.Bytes(), &entry); err != nil {
			continue // skip malformed lines silently
		}
		if !filter(entry) {
			continue
		}
		for _, sink := range sinks {
			if err := sink.Write(entry); err != nil {
				slog.Warn("sink write failed", "err", err)
			}
		}
	}
	return scanner.Err()
}

// parseFilter is a stub — real implementation pending. See TODO in README.
func parseFilter(expr string) (func(map[string]any) bool, error) {
	if expr == "" {
		return func(_ map[string]any) bool { return true }, nil
	}
	return func(_ map[string]any) bool { return true }, nil
}
