#include "gtest/gtest.h"
#include "libCDF++.h"
#include <vector>

struct testInput
{
    std::string file;
    bool expectGoodMagic;
};


namespace {
class CdfTestCDR : public ::testing::TestWithParam<testInput> {
protected:
    CdfTestCDR() {
        // You can do set-up work for each test here.
    }

    virtual ~CdfTestCDR() {
        // You can do clean-up work that doesn't throw exceptions here.
    }

    // If the constructor and destructor are not enough for setting up
    // and cleaning up each test, you can define the following methods:

    virtual void SetUp() {
        // Code here will be called immediately after the constructor (right
        // before each test).
    }

    virtual void TearDown() {
        // Code here will be called immediately after each test (right
        // before the destructor).
    }
};
};

TEST_P(CdfTestCDR, Magic) {
    auto input = GetParam();
    Cdf f(input.file);
    EXPECT_EQ(input.expectGoodMagic, f.isOpened());
}

const testInput testInputs[] = {
    {TEST_DATA_DIR"/random.cdf",false},
    {TEST_DATA_DIR"/cacsst2.cdf",true}
};

INSTANTIATE_TEST_CASE_P(CDR_Magic,CdfTestCDR,::testing::ValuesIn(testInputs));

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
