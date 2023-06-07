using Xunit;
using BLComponent;
#nullable disable

namespace BLModelTests
{
    public class AuthorTest
    {
        public static IEnumerable<object[]> TestCorrectDataAuthorValidation
        {
            get
            {
                yield return new object[] { 1, "Пушкин Александр", new DateOnly(1799, 5, 26), new DateOnly(1837, 1, 29), "../TableData/AuthorsPhoto/pushkin.png", "биография поэта..." };
                yield return new object[] { 1, "Пушкин Александр", null, new DateOnly(1837, 1, 29), "../TableData/AuthorsPhoto/pushkin.png", "биография поэта..." };
                yield return new object[] { 1, "Пушкин Александр", new DateOnly(1799, 5, 26), null, "../TableData/AuthorsPhoto/pushkin.png", "биография поэта..." };
                yield return new object[] { 1, "Пушкин Александр", null, null, "../TableData/AuthorsPhoto/pushkin.png", "биография поэта..." };
            }
        }
        
        [Theory]
        [MemberData(nameof(TestCorrectDataAuthorValidation))]
        public void Author_Creation_PositiveTest(ushort id, string initials, DateOnly? birth_date, DateOnly? death_date, string photo_path, string biography)
        {
            Author Obj = new Author(id, initials, birth_date, death_date, photo_path, biography);
            
            Assert.Equal(id, Obj.ID);
            Assert.Equal(initials, Obj.Initials);
            Assert.Equal(birth_date, Obj.BirthDate);
            Assert.Equal(death_date, Obj.DeathDate);
            Assert.Equal(photo_path, Obj.PhotoPath);
            Assert.Equal(biography, Obj.Biography);
        }

        public static IEnumerable<object[]> TestAuthorDataArgumentNullException
        {
            get
            {
                yield return new object[] { 1, null, new DateOnly(1799, 5, 26), new DateOnly(1837, 1, 29), "../TableData/AuthorsPhoto/pushkin.png", "биография поэта..." };
                yield return new object[] { 1, "", new DateOnly(1799, 5, 26), new DateOnly(1837, 1, 29), "../TableData/AuthorsPhoto/pushkin.png", "биография поэта..." };
                yield return new object[] { 1, "     ", new DateOnly(1799, 5, 26), new DateOnly(1837, 1, 29), "../TableData/AuthorsPhoto/pushkin.png", "биография поэта..." };
                yield return new object[] { 1, "Пушкин Александр", new DateOnly(1799, 5, 26), new DateOnly(1837, 1, 29), null, "биография поэта..." };
                yield return new object[] { 1, "Пушкин Александр", new DateOnly(1799, 5, 26), new DateOnly(1837, 1, 29), "", "биография поэта..." };
                yield return new object[] { 1, "Пушкин Александр", new DateOnly(1799, 5, 26), new DateOnly(1837, 1, 29), "    ", "биография поэта..." };
                yield return new object[] { 1, "Пушкин Александр", new DateOnly(1799, 5, 26), new DateOnly(1837, 1, 29), "../TableData/AuthorsPhoto/pushkin.png", null };
                yield return new object[] { 1, "Пушкин Александр", new DateOnly(1799, 5, 26), new DateOnly(1837, 1, 29), "../TableData/AuthorsPhoto/pushkin.png", "" };
                yield return new object[] { 1, "Пушкин Александр", new DateOnly(1799, 5, 26), new DateOnly(1837, 1, 29), "../TableData/AuthorsPhoto/pushkin.png", "    " };
            }
        }

        [Theory]
        [MemberData(nameof(TestAuthorDataArgumentNullException))]
        public void Author_Creation_ArgumentNullException_NegativeTest(ushort id, string initials, DateOnly? birth_date, DateOnly? death_date, string photo_path, string biography)
        {
            Assert.Throws<ArgumentNullException>(() => new Author(id, initials, birth_date, death_date, photo_path, biography));
        }

        public static IEnumerable<object[]> TestAuthorDataArgumentException
        {
            get
            {
                yield return new object[] { 0, "Пушкин Александр", new DateOnly(1799, 5, 26), new DateOnly(1837, 1, 29), "../TableData/AuthorsPhoto/pushkin.png", "биография поэта..." };
                yield return new object[] { 1, "Pushkin Alex", new DateOnly(1799, 5, 26), new DateOnly(1837, 1, 29), "../TableData/AuthorsPhoto/pushkin.png", "биография поэта..." };
                yield return new object[] { 1, "пушкин александр", new DateOnly(1799, 5, 26), new DateOnly(1837, 1, 29), "../TableData/AuthorsPhoto/pushkin.png", "биография поэта..." };
                yield return new object[] { 1, "Пушкин Александр ", new DateOnly(1799, 5, 26), new DateOnly(1837, 1, 29), "../TableData/AuthorsPhoto/pushkin.png", "биография поэта..." };
                yield return new object[] { 1, "Пушкин Александр", new DateOnly(1499, 5, 26), new DateOnly(1837, 1, 29), "../TableData/AuthorsPhoto/pushkin.png", "биография поэта..." };
                yield return new object[] { 1, "Пушкин Александр", new DateOnly(2222, 5, 26), new DateOnly(1837, 1, 29), "../TableData/AuthorsPhoto/pushkin.png", "биография поэта..." };
                yield return new object[] { 1, "Пушкин Александр", new DateOnly(1799, 5, 26), new DateOnly(1499, 1, 29), "../TableData/AuthorsPhoto/pushkin.png", "биография поэта..." };
                yield return new object[] { 1, "Пушкин Александр", new DateOnly(1799, 5, 26), new DateOnly(2222, 1, 29), "../TableData/AuthorsPhoto/pushkin.png", "биография поэта..." };
                yield return new object[] { 1, "Пушкин Александр", new DateOnly(1900, 5, 26), new DateOnly(1837, 1, 29), "../TableData/AuthorsPhoto/pushkin.png", "биография поэта..." };
                yield return new object[] { 1, "Пушкин Александр", new DateOnly(1799, 5, 26), new DateOnly(2000, 1, 29), "../TableData/AuthorsPhoto/pushkin.png", "биография поэта..." };
                yield return new object[] { 1, "Пушкин Александр", new DateOnly(1799, 5, 26), new DateOnly(1837, 1, 29), "pushkin.png", "биография поэта..." };
            }
        }

        [Theory]
        [MemberData(nameof(TestAuthorDataArgumentException))]
        public void Author_Creation_ArgumentException_NegativeTest(ushort id, string initials, DateOnly? birth_date, DateOnly? death_date, string photo_path, string biography)
        {
            Assert.Throws<ArgumentException>(() => new Author(id, initials, birth_date, death_date, photo_path, biography));
        }
    }
}