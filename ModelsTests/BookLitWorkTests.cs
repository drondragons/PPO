using Xunit;
using BLComponent;
#nullable disable

namespace BLModelTests
{
    public class BookLitWorkTest
    {
        [Theory]
        [InlineData(1, 1, 1)]
        [InlineData(2, 1, 3)]
        public void BookLitWork_Creation_PositiveTest(uint id, ushort book_id, ushort lit_work_id)
        {
            BookLitWork Obj = new BookLitWork(id, book_id, lit_work_id);

            Assert.Equal(id, Obj.ID);
            Assert.Equal(book_id, Obj.BookID);
            Assert.Equal(lit_work_id, Obj.LitWorkID);
        }

        [Theory]
        [InlineData(0, 1, 1)]
        [InlineData(1, 0, 1)]
        [InlineData(1, 1, 0)]
        public void BookLitWork_Creation_ArgumentException_NegativeTest(uint id, ushort book_id, ushort lit_work_id) 
        {
            Assert.Throws<ArgumentException>(() => new BookLitWork(id, book_id, lit_work_id));
        }
    }
}