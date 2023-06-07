using Xunit;
using BLComponent;
#nullable disable

namespace BLModelTests 
{
    public class RoleTest 
    {
        [Theory]
        [InlineData(1, "гость")]
        [InlineData(2, "читатель")]
        [InlineData(3, "библиотекарь")]
        public void Role_Creation_PositiveTest(byte id, string role) 
        {
            Role Obj = new Role(id, role);

            Assert.Equal(id, Obj.ID);
            Assert.Equal(role, Obj.Name);
        }

        [Theory]
        [InlineData(0, "гость")]
        public void Role_Creation_ArgumentException_NegativeTest(byte id, string role) 
        {
            Assert.Throws<ArgumentException>(() => new Role(id, role));
        }

        [Theory]
        [InlineData(1, "")]
        [InlineData(2, "              ")]
        [InlineData(4, null)]
        public void Role_Creation_ArgumentNullException_NegativeTest(byte id, string role) 
        {
            Assert.Throws<ArgumentNullException>(() => new Role(id, role));
        }
    }
}