using Xunit;
using BLComponent;
#nullable disable

namespace BLModelTests 
{
    public class GenreTest 
    {
        [Theory]
        [InlineData(1, "фантастика", "Описание жанра")]
        [InlineData(2, "роман", "Описание жанра")]
        [InlineData(3, "проза", "Описание жанра")]
        public void Genre_Creation_PositiveTest(ushort id, string title, string description) 
        {
            Genre Obj = new Genre(id, title, description);

            Assert.Equal(id, Obj.ID);
            Assert.Equal(title, Obj.Title);
            Assert.Equal(description, Obj.Description);
        }

        [Theory]
        [InlineData(0, "роман", "Описание жанра")]
        public void Genre_Creation_ArgumentException_NegativeTest(ushort id, string title, string description) 
        {
            Assert.Throws<ArgumentException>(() => new Genre(id, title, description));
        }

        [Theory]
        [InlineData(1, null, "Описание жанра")]
        [InlineData(2, "", "Описание жанра")]
        [InlineData(4, "    ", "Описание жанра")]
        [InlineData(1, "фантастика", null)]
        [InlineData(1, "фантастика", "")]
        [InlineData(1, "фантастика", "    ")]
        public void Genre_Creation_ArgumentNullException_NegativeTest(ushort id, string title, string description) 
        {
            Assert.Throws<ArgumentNullException>(() => new Genre(id, title, description));
        }
    }
}