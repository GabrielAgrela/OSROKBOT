import psutil

def get_allocation_base_from_pid(pid):
    process = psutil.Process(pid)

    mem_maps = list(process.memory_maps())
    # Grouping by path to combine all the mappings of the same module
    grouped_maps = {}
    for entry in mem_maps:
        if entry.path not in grouped_maps:
            grouped_maps[entry.path] = []
        grouped_maps[entry.path].append(entry)

    for path, mappings in grouped_maps.items():
        # Calculating the combined size of all memory segments of a module
        total_size = sum([m.rss for m in mappings])
        # If the total size matches our desired range, return the start address of the first segment
        # Find previous large memory region
        prev_regions = [m for m in mem_maps if 0x3500000000 <= m.rss <= 0x3800000000]
        if prev_regions:  # Check if any region with the size range 3500000000 to 3800000000 exists
            prev_region = prev_regions[-1]  # Assuming you're referring to the latest one
            # Check if our desired region comes immediately after the previous large memory region
            if mappings[0].addr > prev_region.addr:
                return hex(mappings[0].addr)
    return None

pid = 19576
allocation_base = get_allocation_base_from_pid(pid)
if allocation_base:
    print(f"Allocation base for PID {pid}: {allocation_base}")
else:
    print(f"Could not determine allocation base for PID {pid}.")
