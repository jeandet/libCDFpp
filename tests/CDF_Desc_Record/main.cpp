#include "gtest/gtest.h"
#include "libCDF++.h"

namespace {

class CdfTest : public ::testing::Test {
 protected:
  CdfTest() {
    // You can do set-up work for each test here.
  }

  virtual ~CdfTest() {
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

TEST_F(CdfTest, OpenWrongFile) {
  const std::string file = "wrongCDF.cdf";
  Cdf f(file);
  EXPECT_EQ(false, f.isOpened());
}

TEST_F(CdfTest, OpenExistingFile) {
  const std::string file = TEST_DATA_DIR"/cacsst2.cdf";
  Cdf f(file);
  EXPECT_EQ(true, f.isOpened());
}

TEST_F(CdfTest, WrongMagic) {
  const std::string file = TEST_DATA_DIR"/random.cdf";
  Cdf f(file);
  EXPECT_EQ(false, f.isOpened());
}

TEST_F(CdfTest, GoodMagic) {
  const std::string file = TEST_DATA_DIR"/cacsst2.cdf";
  Cdf f(file);
  EXPECT_EQ(true, f.isOpened());
}

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
