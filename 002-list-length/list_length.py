def list_length(single_method_list):
    # Implement this function and write some tests for it.
    # Performance is important
    prev, next = 0, 1
    if single_method_list.get(0) is None:
        return 0
    elif single_method_list.get(1) is None:
        return 1
    else:
        while prev < next:
            if single_method_list.get(next) is not None:
                prev = next
                next *= 2
            else:
                next = int(prev + (next - prev) / 2)
        return prev + 1
