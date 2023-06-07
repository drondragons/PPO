using Xunit;
using BLComponent;
#nullable disable

namespace BLModelTests 
{
    public class UserTest
    {
        public static IEnumerable<object[]> TestCorrectDataUserValidation
        {
            get
            {
                yield return new object[] { 1, "andrew222", "andrew@mail.com", "Андрей Трунов", "81234567890", "123456789", new DateOnly(2000, 1, 1), true, 1 };
                yield return new object[] { 1, "andrew222", "andrew@mail.com", "Андрей Трунов", "81234567890", "123456789", null, true, 1 };
                yield return new object[] { 1, "andrew222", "andrew@mail.com", "Андрей Трунов", null, "123456789", new DateOnly(2000, 1, 1), true, 1 };
                yield return new object[] { 1, "andrew222", "andrew@mail.com", "Андрей Трунов", null, "123456789", null, true, 1 };
            }
        }
        
        [Theory]
        [MemberData(nameof(TestCorrectDataUserValidation))]
        public void User_Creation_PositiveTest(ushort id, string login, string email, string initials, string phone_number, string password, DateOnly? birth_date, bool actaulity, byte role_id)
        {
            User Obj = new User(id, login, email, initials, phone_number, password, birth_date, actaulity, role_id);
            
            Assert.Equal(id, Obj.ID);
            Assert.Equal(login, Obj.Login);
            Assert.Equal(email, Obj.Email);
            Assert.Equal(initials, Obj.Initials);
            Assert.Equal(role_id, Obj.RoleID);
            Assert.Equal(phone_number, Obj.PhoneNumber);
            Assert.Equal(password, Obj.Password);
            Assert.Equal(birth_date, Obj.BirthDate);
            Assert.Equal(actaulity, Obj.Actuality);
        }

        public static IEnumerable<object[]> TestUserDataArgumentNullException
        {
            get
            {
                yield return new object[] { 1, null, "andrew@mail.com", "Андрей Трунов", "81234567890", "123456789", new DateOnly(2000, 1, 1), true, 1};
                yield return new object[] { 1, "", "andrew@mail.com", "Андрей Трунов", "81234567890", "123456789", new DateOnly(2000, 1, 1), true, 1};
                yield return new object[] { 1, "    ", "andrew@mail.com", "Андрей Трунов", "81234567890", "123456789", new DateOnly(2000, 1, 1), true, 1};
                yield return new object[] { 1, "andrew222", null, "Андрей Трунов", "81234567890", "123456789", new DateOnly(2000, 1, 1), true, 1};
                yield return new object[] { 1, "andrew222", "", "Андрей Трунов", "81234567890", "123456789", new DateOnly(2000, 1, 1), true, 1};
                yield return new object[] { 1, "andrew222", "    ", "Андрей Трунов", "81234567890", "123456789", new DateOnly(2000, 1, 1), true, 1};
                yield return new object[] { 1, "andrew222", "andrew@mail.com", null, "81234567890", "123456789", new DateOnly(2000, 1, 1), true, 1};
                yield return new object[] { 1, "andrew222", "andrew@mail.com", "", "81234567890", "123456789", new DateOnly(2000, 1, 1), true, 1};
                yield return new object[] { 1, "andrew222", "andrew@mail.com", "     ", "81234567890", "123456789", new DateOnly(2000, 1, 1), true, 1};
                yield return new object[] { 1, "andrew222", "andrew@mail.com", "Андрей Трунов", "81234567890", null, new DateOnly(2000, 1, 1), true, 1};
                yield return new object[] { 1, "andrew222", "andrew@mail.com", "Андрей Трунов", "81234567890", "", new DateOnly(2000, 1, 1), true, 1};
                yield return new object[] { 1, "andrew222", "andrew@mail.com", "Андрей Трунов", "81234567890", "     ", new DateOnly(2000, 1, 1), true, 1};
            }
        }

        [Theory]
        [MemberData(nameof(TestUserDataArgumentNullException))]
        public void User_Creation_ArgumentNullException_NegativeTest(ushort id, string login, string email, string initials, string phone_number, string password, DateOnly? birth_date, bool actaulity, byte role_id)
        {
            Assert.Throws<ArgumentNullException>(() => new User(id, login, email, initials, phone_number, password, birth_date, actaulity, role_id));
        }

        public static IEnumerable<object[]> TestUserDataArgumentException
        {
            get
            {
                yield return new object[] { 0, "andrew222", "andrew@mail.com", "Андрей Трунов", "81234567890", "123456789", new DateOnly(2000, 1, 1), true, 1 };
                yield return new object[] { 1, "andrew", "andrew@mail.com", "Андрей Трунов", "81234567890", "123456789", new DateOnly(2000, 1, 1), true, 1 };
                yield return new object[] { 1, "andrew222nsinviusnvisndvvunsdiucnsnisdncsnvjnvrebnvsnvkjsdncvjdsnc", "andrew@mail.com", "Андрей Трунов", "81234567890", "123456789", new DateOnly(2000, 1, 1), true, 1 };
                yield return new object[] { 1, "Андрей22222", "andrew@mail.com", "Андрей Трунов", "81234567890", "123456789", new DateOnly(2000, 1, 1), true, 1 };
                yield return new object[] { 1, "andrew222", "andrewmail.com", "Андрей Трунов", "81234567890", "123456789", new DateOnly(2000, 1, 1), true, 1 };
                yield return new object[] { 1, "andrew222", "andrew@mail.c", "Андрей Трунов", "81234567890", "123456789", new DateOnly(2000, 1, 1), true, 1 };
                yield return new object[] { 1, "andrew222", "andrew@mailcom", "Андрей Трунов", "81234567890", "123456789", new DateOnly(2000, 1, 1), true, 1 };
                yield return new object[] { 1, "andrew222", "andrew@mail.com", "Andrew Trunov", "81234567890", "123456789", new DateOnly(2000, 1, 1), true, 1 };
                yield return new object[] { 1, "andrew222", "andrew@mail.com", "андрей трунов", "81234567890", "123456789", new DateOnly(2000, 1, 1), true, 1 };
                yield return new object[] { 1, "andrew222", "andrew@mail.com", "Андрей Трунов ", "81234567890", "123456789", new DateOnly(2000, 1, 1), true, 1 };
                yield return new object[] { 1, "andrew222", "andrew@mail.com", "Андрей Трунов", "8123456789", "123456789", new DateOnly(2000, 1, 1), true, 1  };
                yield return new object[] { 1, "andrew222", "andrew@mail.com", "Андрей Трунов", "812345678901", "123456789", new DateOnly(2000, 1, 1), true, 1  };
                yield return new object[] { 1, "andrew222", "andrew@mail.com", "Андрей Трунов", "+7234567890", "123456789", new DateOnly(2000, 1, 1), true, 1  };
                yield return new object[] { 1, "andrew222", "andrew@mail.com", "Андрей Трунов", "81234567890", "123456789", new DateOnly(2222, 1, 1), true, 1  };
                yield return new object[] { 1, "andrew222", "andrew@mail.com", "Андрей Трунов", "81234567890", "123456789", new DateOnly(2000, 1, 1), true, 0  };
            }
        }

        [Theory]
        [MemberData(nameof(TestUserDataArgumentException))]
        public void User_Creation_ArgumentException_NegativeTest(ushort id, string login, string email, string initials, string phone_number, string password, DateOnly? birth_date, bool actaulity, byte role_id)
        {
            Assert.Throws<ArgumentException>(() => new User(id, login, email, initials, phone_number, password, birth_date, actaulity, role_id));
        }
    }
}