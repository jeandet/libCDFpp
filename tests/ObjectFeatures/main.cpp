#include "gtest/gtest.h"
#include "libCDF.h"

namespace {

class CdfTestObjectFeatures : public ::testing::Test {
 protected:
  CdfTestObjectFeatures() {
    // You can do set-up work for each test here.
  }

  virtual ~CdfTestObjectFeatures() {
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

TEST_F(CdfTestObjectFeatures, IsCopyable) {
  EXPECT_EQ(true, std::is_copy_constructible<Cdf>::value);
  EXPECT_EQ(true, std::is_copy_assignable<Cdf>::value);
}

TEST_F(CdfTestObjectFeatures, IsMoveable) {
    EXPECT_EQ(true, std::is_move_constructible<Cdf>::value);
    EXPECT_EQ(true, std::is_move_assignable<Cdf>::value);
}

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
