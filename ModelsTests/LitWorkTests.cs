using Xunit;
using BLComponent;
#nullable disable

namespace BLModelTests
{
    public class LitWorkTest
    {
        public static IEnumerable<object[]> TestCorrectDataLitWorkValidation
        {
            get
            {
                yield return new object[] { 1, "Название произведения", (ushort?)1900, "Краткое описание произведения", "../TableData/BooksEpub/default.epub"};
                yield return new object[] { 1, "Название произведения", null, "Краткое описание произведения", "../TableData/BooksEpub/default.epub"};
                yield return new object[] { 1, "Название произведения", (ushort?)1900, "Краткое описание произведения", null};
                yield return new object[] { 1, "Название произведения", null, "Краткое описание произведения", null};
            }
        }

        [Theory]
        [MemberData(nameof(TestCorrectDataLitWorkValidation))]
        public void LitWork_Creation_PositiveTest(ushort id, string title, ushort? writing_year, string description, string text_path)
        {
            LitWork Obj = new LitWork(id, title, writing_year, description, text_path);

            Assert.Equal(id, Obj.ID);
            Assert.Equal(title, Obj.Title);
            Assert.Equal(writing_year, Obj.WritingYear);
            Assert.Equal(description, Obj.Description);
            Assert.Equal(text_path, Obj.TextPath);
        }

        public static IEnumerable<object[]> TestLitWorkDataArgumentNullException
        {
            get
            {
                yield return new object[] { 1, null, (ushort?)1900, "Краткое описание произведения", "../TableData/BooksEpub/default.epub"};
                yield return new object[] { 1, "", (ushort?)1900, "Краткое описание произведения", "../TableData/BooksEpub/default.epub"};
                yield return new object[] { 1, "    ", (ushort?)1900, "Краткое описание произведения", "../TableData/BooksEpub/default.epub"};
                yield return new object[] { 1, "Название произведения", (ushort?)1900, null, "../TableData/BooksEpub/default.epub"};
                yield return new object[] { 1, "Название произведения", (ushort?)1900, "", "../TableData/BooksEpub/default.epub"};
                yield return new object[] { 1, "Название произведения", (ushort?)1900, "     ", "../TableData/BooksEpub/default.epub"};
            }
        }

        [Theory]
        [MemberData(nameof(TestLitWorkDataArgumentNullException))]
        public void LitWork_Creation_ArgumentNullException_NegativeTest(ushort id, string title, ushort? writing_year, string description, string text_path)
        {
            Assert.Throws<ArgumentNullException>(() => new LitWork(id, title, writing_year, description, text_path));
        }

        public static IEnumerable<object[]> TestLitWorkDataArgumentException
        {
            get
            {
                yield return new object[] { 0, "Название произведения", (ushort?)1900, "Краткое описание произведения", "../TableData/BooksEpub/default.epub"};
                yield return new object[] { 1, "Название произведения", (ushort?)1499, "Краткое описание произведения", "../TableData/BooksEpub/default.epub"};
                yield return new object[] { 1, "Название произведения", (ushort?)2222, "Краткое описание произведения", "../TableData/BooksEpub/default.epub"};
                yield return new object[] { 1, "Название произведения", (ushort?)1900, "Краткое описание произведения", "default.epub"};
            }
        }

        [Theory]
        [MemberData(nameof(TestLitWorkDataArgumentException))]
        public void LitWork_Creation_ArgumentException_NegativeTest(ushort id, string title, ushort? writing_year, string description, string text_path)
        {
            Assert.Throws<ArgumentException>(() => new LitWork(id, title, writing_year, description, text_path));
        }
    }
}