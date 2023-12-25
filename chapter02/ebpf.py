#!/usr/bin/python3
from bcc import BPF

# BPF program
program = r"""
int hello(void *ctx) {
    bpf_trace_printk("Hello eBPF!\n");
    return 0;
}
"""

# Create BPF object
b = BPF(text=program)

# Attach the BPF program to a trace point
b.attach_tracepoint(tp="syscalls", fn_name="hello")

# Print trace events
print("Tracing... Ctrl+C to stop.")
b.trace_print()
