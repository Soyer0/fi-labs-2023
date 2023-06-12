#pragma once
#include "LFSR.hpp"

class Geffe
{
    LFSR L1;
    LFSR L2;
    LFSR L3;

public:
    Geffe(const LFSR &_L1, const LFSR &_L2, const LFSR &_L3);

    std::vector<uint8_t> generate(uint32_t init_l1, uint32_t init_l2, uint32_t init_l3, size_t lenght);
};

Geffe::Geffe(const LFSR &_L1, const LFSR &_L2, const LFSR &_L3)
    : L1{_L1}, L2{_L2}, L3{_L3} {};

// Fast enought for out task
std::vector<uint8_t> Geffe::generate(uint32_t init_l1, uint32_t init_l2, uint32_t init_l3, size_t lenght)
{
    std::vector<uint8_t> res(lenght);

    auto X = L1.generate_from_fill(init_l1, lenght);
    auto Y = L2.generate_from_fill(init_l2, lenght);
    auto S = L3.generate_from_fill(init_l3, lenght);

    for (int i = 0; i < lenght; ++i)
    {
        if (S[i] == uint8_t(1))
            res[i] = X[i];
        else
            res[i] = Y[i];
    }

    return res;
}