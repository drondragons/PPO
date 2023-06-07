using Xunit;
using BLComponent;
#nullable disable

namespace BLModelTests
{
    public class CountryTest
    {
        [Theory]
        [InlineData(1, "Россия")]
        [InlineData(2, "Франция")]
        public void Country_Creation_PositiveTest(byte id, string title)
        {
            Country Obj = new Country(id, title);

            Assert.Equal(id, Obj.ID);
            Assert.Equal(title, Obj.Title);
        }

        [Theory]
        [InlineData(1, null)]
        [InlineData(1, "")]
        [InlineData(1, "   ")]
        public void Country_Creation_ArgumentNullException_NegativeTest(byte id, string title) 
        {
            Assert.Throws<ArgumentNullException>(() => new Country(id, title));
        }

        [Theory]
        [InlineData(0, "Россия")]
        public void Country_Creation_ArgumentException_NegativeTest(byte id, string title) 
        {
            Assert.Throws<ArgumentException>(() => new Country(id, title));
        }
    }
}