using Xunit;
using BLComponent;
#nullable disable

namespace BLModelTests
{
    public class BookRegistrationTest
    {
        public static IEnumerable<object[]> TestCorrectDataBookRegistrationValidation
        {
            get
            {
                yield return new object[] { 1, 1, 1, 1, 150, new DateTime(2000, 1, 1, 10, 0, 0) };
            }
        }

        [Theory]
        [MemberData(nameof(TestCorrectDataBookRegistrationValidation))]
        public void BookRegistration_Creation_PositiveTest(uint id, ushort user_id, ushort book_id, byte book_status_id, ushort book_amount, DateTime? registration_date)
        {
            BookRegistration Obj = new BookRegistration(id, user_id, book_id, book_status_id, book_amount, registration_date);

            Assert.Equal(id, Obj.ID);
            Assert.Equal(user_id, Obj.UserID);
            Assert.Equal(book_id, Obj.BookID);
            Assert.Equal(book_status_id, Obj.BookStatusID);
            Assert.Equal(book_amount, Obj.BookAmount);
            Assert.Equal(registration_date, Obj.RegistrationDate);
        }

        public static IEnumerable<object[]> TestBookRegistrationDataArgumentNullException
        {
            get
            {
                yield return new object[] { 1, 1, 1, 1, 150, null };
            }
        }

        [Theory]
        [MemberData(nameof(TestBookRegistrationDataArgumentNullException))]
        public void BookRegistration_Creation_ArgumentNullException_NegativeTest(uint id, ushort user_id, ushort book_id, byte book_status_id, ushort book_amount, DateTime? registration_date)
        {
            Assert.Throws<ArgumentNullException>(() => new BookRegistration(id, user_id, book_id, book_status_id, book_amount, registration_date));
        }

        public static IEnumerable<object[]> TestBookRegistrationDataArgumentException
        {
            get
            {
                yield return new object[] { 0, 1, 1, 1, 150, new DateTime(2000, 1, 1, 10, 0, 0) };
                yield return new object[] { 1, 0, 1, 1, 150, new DateTime(2000, 1, 1, 10, 0, 0) };
                yield return new object[] { 1, 1, 0, 1, 150, new DateTime(2000, 1, 1, 10, 0, 0) };
                yield return new object[] { 1, 1, 1, 0, 150, new DateTime(2000, 1, 1, 10, 0, 0) };
                yield return new object[] { 1, 1, 1, 1, 0, new DateTime(2000, 1, 1, 10, 0, 0) };
                yield return new object[] { 1, 1, 1, 1, 150, new DateTime(2222, 1, 1, 10, 0, 0) };
            }
        }

        [Theory]
        [MemberData(nameof(TestBookRegistrationDataArgumentException))]
        public void BookRegistration_Creation_ArgumentException_NegativeTest(uint id, ushort user_id, ushort book_id, byte book_status_id, ushort book_amount, DateTime? registration_date)
        {
            Assert.Throws<ArgumentException>(() => new BookRegistration(id, user_id, book_id, book_status_id, book_amount, registration_date));
        }
    }
}