#pragma once
#include <vector>
#include <cstdint>

// Limit polynomial deg with 32 bits (uint32_t)
// That is sufficient for our task
class LFSR
{
    uint32_t filling;
    const uint32_t __mask_for_bit_to_pop = 1;
    uint32_t __mask_for_bit_to_set;
    uint8_t max_bit_n;
    uint32_t recurvia;

public:
    LFSR(uint32_t recurv_coefs, uint8_t poly_deg);

    std::vector<uint8_t> generate_from_fill(uint32_t initial_fill, uint64_t length);
};

LFSR::LFSR(uint32_t recurv_coefs, uint8_t poly_deg) : max_bit_n{poly_deg - 1}, recurvia{recurv_coefs}
{
    __mask_for_bit_to_set = (1 << max_bit_n);
};

std::vector<uint8_t> LFSR::generate_from_fill(uint32_t _filling, uint64_t length)
{
    filling = _filling;
    std::vector<uint8_t> feedback(length);

    for (uint64_t i = 0; i < length; ++i)
    {
        feedback[i] = uint8_t(filling & __mask_for_bit_to_pop);
        filling = (filling >> 1) ^ ((__builtin_popcount(filling & recurvia) & 1u) << max_bit_n);
    }

    return feedback;
}
