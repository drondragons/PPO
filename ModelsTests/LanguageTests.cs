using Xunit;
using BLComponent;
#nullable disable

namespace BLModelTests
{
    public class LanguageTest
    {
        [Theory]
        [InlineData(1, "русский")]
        [InlineData(2, "английский")]
        public void Language_Creation_PositiveTest(byte id, string title)
        {
            Language Obj = new Language(id, title);

            Assert.Equal(id, Obj.ID);
            Assert.Equal(title, Obj.Title);
        }

        [Theory]
        [InlineData(1, null)]
        [InlineData(1, "")]
        [InlineData(1, "   ")]
        public void Language_Creation_ArgumentNullException_NegativeTest(byte id, string title) 
        {
            Assert.Throws<ArgumentNullException>(() => new Language(id, title));
        }

        [Theory]
        [InlineData(0, "русский")]
        public void Language_Creation_ArgumentException_NegativeTest(byte id, string title) 
        {
            Assert.Throws<ArgumentException>(() => new Language(id, title));
        }
    }
}