using Xunit;
using BLComponent;
#nullable disable

namespace BLModelTests
{
    public class BookTest
    {
        public static IEnumerable<object[]> TestCorrectDataBookValidation
        {
            get
            {
                yield return new object[] { 1, "Название книги", "901-2903-1192-23", 100, 100, 2021, 1, 100.00, "Аннотация для книги", "../TableData/BooksPhoto/default.png", null };
                yield return new object[] { 1, "Название книги", "901-2903-1192-23", 100, 100, 2021, 1, 100.00, "Аннотация для книги", "../TableData/BooksPhoto/default.png", "второй зал, третья полка" };
            }
        }

        [Theory]
        [MemberData(nameof(TestCorrectDataBookValidation))]
        public void Book_Creation_PositiveTest(ushort id, string title, string isbn, ushort total_pages, ushort amount, ushort publication_year, ushort publisher_id, decimal price, string annotation, string cover_photo_path, string library_location)
        {
            Book Obj = new Book(id, title, isbn, total_pages, amount, publication_year, publisher_id, price, annotation, cover_photo_path, library_location);

            Assert.Equal(id, Obj.ID);
            Assert.Equal(title, Obj.Title);
            Assert.Equal(isbn, Obj.ISBN);
            Assert.Equal(total_pages, Obj.TotalPages);
            Assert.Equal(amount, Obj.Amount);
            Assert.Equal(publication_year, Obj.PublicationYear);
            Assert.Equal(publisher_id, Obj.PublisherID);
            Assert.Equal(price, Obj.Price);
            Assert.Equal(annotation, Obj.Annotation);
            Assert.Equal(cover_photo_path, Obj.CoverPhotoPath);
            Assert.Equal(library_location, Obj.LibraryLocation);
        }

        public static IEnumerable<object[]> TestBookDataArgumentNullException
        {
            get
            {
                yield return new object[] { 1, null, "901-2903-1192-23", 100, 100, 2021, 1, 100.00, "Аннотация для книги", "../TableData/BooksPhoto/default.png", null };
                yield return new object[] { 1, "", "901-2903-1192-23", 100, 100, 2021, 1, 100.00, "Аннотация для книги", "../TableData/BooksPhoto/default.png", null };
                yield return new object[] { 1, "   ", "901-2903-1192-23", 100, 100, 2021, 1, 100.00, "Аннотация для книги", "../TableData/BooksPhoto/default.png", null };
                yield return new object[] { 1, "Название книги", null, 100, 100, 2021, 1, 100.00, "Аннотация для книги", "../TableData/BooksPhoto/default.png", null };
                yield return new object[] { 1, "Название книги", "", 100, 100, 2021, 1, 100.00, "Аннотация для книги", "../TableData/BooksPhoto/default.png", null };
                yield return new object[] { 1, "Название книги", "    ", 100, 100, 2021, 1, 100.00, "Аннотация для книги", "../TableData/BooksPhoto/default.png", null };
                yield return new object[] { 1, "Название книги", "901-2903-1192-23", 100, 100, 2021, 1, 100.00, null, "../TableData/BooksPhoto/default.png", null };
                yield return new object[] { 1, "Название книги", "901-2903-1192-23", 100, 100, 2021, 1, 100.00, "", "../TableData/BooksPhoto/default.png", null };
                yield return new object[] { 1, "Название книги", "901-2903-1192-23", 100, 100, 2021, 1, 100.00, "    ", "../TableData/BooksPhoto/default.png", null };
                yield return new object[] { 1, "Название книги", "901-2903-1192-23", 100, 100, 2021, 1, 100.00, "Аннотация для книги", null, null };
                yield return new object[] { 1, "Название книги", "901-2903-1192-23", 100, 100, 2021, 1, 100.00, "Аннотация для книги", "", null };
                yield return new object[] { 1, "Название книги", "901-2903-1192-23", 100, 100, 2021, 1, 100.00, "Аннотация для книги", "     ", null };
            }
        }

        [Theory]
        [MemberData(nameof(TestBookDataArgumentNullException))]
        public void Book_Creation_ArgumentNullException_NegativeTest(ushort id, string title, string isbn, ushort total_pages, ushort amount, ushort publication_year, ushort publisher_id, decimal price, string annotation, string cover_photo_path, string library_location)
        {
            Assert.Throws<ArgumentNullException>(() => new Book(id, title, isbn, total_pages, amount, publication_year, publisher_id, price, annotation, cover_photo_path, library_location));
        }

        public static IEnumerable<object[]> TestBookDataArgumentException
        {
            get
            {
                yield return new object[] { 0, "Название книги", "901-2903-1192-23", 100, 100, 2021, 1, 100.00, "Аннотация для книги", "../TableData/BooksPhoto/default.png", null };
                yield return new object[] { 1, "Название книги", "901-2903-1192", 100, 100, 2021, 1, 100.00, "Аннотация для книги", "../TableData/BooksPhoto/default.png", null };
                yield return new object[] { 1, "Название книги", "901-2903-1192-23-54", 100, 100, 2021, 1, 100.00, "Аннотация для книги", "../TableData/BooksPhoto/default.png", null };
                yield return new object[] { 1, "Название книги", "901 903-030 033", 100, 100, 2021, 1, 100.00, "Аннотация для книги", "../TableData/BooksPhoto/default.png", null };
                yield return new object[] { 1, "Название книги", "901-2903-1192-23", 4, 100, 2021, 1, 100.00, "Аннотация для книги", "../TableData/BooksPhoto/default.png", null };
                yield return new object[] { 1, "Название книги", "901-2903-1192-23", 100, 100, 1499, 1, 100.00, "Аннотация для книги", "../TableData/BooksPhoto/default.png", null };
                yield return new object[] { 1, "Название книги", "901-2903-1192-23", 100, 100, 2222, 1, 100.00, "Аннотация для книги", "../TableData/BooksPhoto/default.png", null };
                yield return new object[] { 1, "Название книги", "901-2903-1192-23", 100, 100, 2021, 0, 100.00, "Аннотация для книги", "../TableData/BooksPhoto/default.png", null };
                yield return new object[] { 1, "Название книги", "901-2903-1192-23", 100, 100, 2021, 1, 0, "Аннотация для книги", "../TableData/BooksPhoto/default.png", null };
                yield return new object[] { 1, "Название книги", "901-2903-1192-23", 100, 100, 2021, 1, 100.00, "Аннотация для книги", "default.png", null };
            }
        }

        [Theory]
        [MemberData(nameof(TestBookDataArgumentException))]
        public void Book_Creation_ArgumentException_NegativeTest(ushort id, string title, string isbn, ushort total_pages, ushort amount, ushort publication_year, ushort publisher_id, decimal price, string annotation, string cover_photo_path, string library_location)
        {
            Assert.Throws<ArgumentException>(() => new Book(id, title, isbn, total_pages, amount, publication_year, publisher_id, price, annotation, cover_photo_path, library_location));
        }
    }
}