using Xunit;
using BLComponent;
#nullable disable

namespace BLModelTests
{
    public class PublisherTest
    {
        [Theory]
        [InlineData(1, "издательство", 1)]
        public void Publisher_Creation_PositiveTest(ushort id, string title, byte country_id)
        {
            Publisher Obj = new Publisher(id, title, country_id);

            Assert.Equal(id, Obj.ID);
            Assert.Equal(title, Obj.Title);
            Assert.Equal(country_id, Obj.CountryID);
        }

        [Theory]
        [InlineData(1, null, 1)]
        [InlineData(1, "", 1)]
        [InlineData(1, "   ", 1)]
        public void Publisher_Creation_ArgumentNullException_NegativeTest(ushort id, string title, byte country_id) 
        {
            Assert.Throws<ArgumentNullException>(() => new Publisher(id, title, country_id));
        }

        [Theory]
        [InlineData(0, "издательство", 1)]
        [InlineData(1, "издательство", 0)]
        public void Publisher_Creation_ArgumentException_NegativeTest(ushort id, string title, byte country_id) 
        {
            Assert.Throws<ArgumentException>(() => new Publisher(id, title, country_id));
        }
    }
}