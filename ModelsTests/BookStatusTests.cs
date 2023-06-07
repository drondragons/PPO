using Xunit;
using BLComponent;
#nullable disable

namespace BLModelTests 
{
    public class BookStatusTest 
    {
        [Theory]
        [InlineData(1, "выдана")]
        [InlineData(100, "возвращена")]
        [InlineData(byte.MaxValue, "добавлена")]
        public void BookStatus_Creation_PositiveTest(byte id, string status) 
        {
            BookStatus Obj = new BookStatus(id, status);

            Assert.Equal(id, Obj.ID);
            Assert.Equal(status, Obj.Name);
        }

        [Theory]
        [InlineData(0, "удалена")]
        public void BookStatus_Creation_ArgumentException_NegativeTest(byte id, string status) 
        {
            Assert.Throws<ArgumentException>(() => new BookStatus(id, status));
        }

        [Theory]
        [InlineData(1, "")]
        [InlineData(5, "              ")]
        [InlineData(9, null)]
        public void BookStatus_Creation_ArgumentNullException_NegativeTest(byte id, string status) 
        {
            Assert.Throws<ArgumentNullException>(() => new BookStatus(id, status));
        }
    }
}