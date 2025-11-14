def pack_complex(i, q):
    """Pack 16-bit signed I/Q into 32-bit unsigned."""
    i &= 0xFFFF
    q &= 0xFFFF
    return (q << 16) | i

def unpack_complex(val):
    """Unpack 32-bit unsigned into signed I/Q (16-bit)."""
    i = val & 0xFFFF
    q = (val >> 16) & 0xFFFF
    # Sign-extend 16-bit values
    if i & 0x8000:
        i -= 0x10000
    if q & 0x8000:
        q -= 0x10000
    return i, q
