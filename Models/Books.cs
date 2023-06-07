#nullable disable

namespace BLComponent
{
    public class Book
    {
        private ushort _id;
        private string _title;
        private string _isbn;
        private ushort _total_pages;
        private ushort _amount;
        private ushort _publication_year;
        private ushort _publisher_id;
        private decimal _price;
        private string _annotation;
        private string _cover_photo_path;
        private string _library_location;

        public ushort ID
        {
            get { return _id; }
            set 
            {
                FieldValidator.Validate(value, 1, ushort.MaxValue, "ID");
                _id = value;
            }
        }

        public string Title
        {
            get { return _title; }
            set 
            {
                FieldValidator.Validate(value, _nullable: false, field_name: "название");
                _title = value;
            }
        }

        public string ISBN
        {
            get { return _isbn; }
            set 
            {
                FieldValidator.Validate(value, 15, 17, false, "^[\\d-]{15,17}$", "ISBN");
                _isbn = value;
            }
        }

        public ushort TotalPages
        {
            get { return _total_pages; }
            set 
            {
                FieldValidator.Validate(value, 5, ushort.MaxValue, "количество страниц");
                _total_pages = value;
            }
        }

        public ushort Amount
        {
            get { return _amount; }
            set 
            {
                FieldValidator.Validate(value, "количество книг");
                _amount = value;
            }
        }

        public ushort PublicationYear
        {
            get { return _publication_year; }
            set 
            {
                FieldValidator.Validate(value, 1500, (ushort)DateTime.Now.Year, "год издания");
                _publication_year = value;
            }
        }

        public ushort PublisherID
        {
            get { return _publisher_id; }
            set 
            {
                FieldValidator.Validate(value, 1, ushort.MaxValue, "publisher ID");
                _publisher_id = value;
            }
        }

        public decimal Price
        {
            get { return _price; }
            set 
            {
                FieldValidator.Validate(value, (decimal)0.01, decimal.MaxValue, "стоимость");
                _price = value;
            }
        }

        public string Annotation
        {
            get { return _annotation; }
            set 
            {
                FieldValidator.Validate(value, _nullable: false, field_name: "аннотация");
                _annotation = value;
            }
        }

        public string CoverPhotoPath
        {
            get { return _cover_photo_path; }
            set 
            {
                FieldValidator.Validate(value, _nullable: false, pattern: "^\\.\\./TableData/BooksPhoto/[0-9а-яА-ЯёЁa-zA-Z_-]+\\.(png|jpg|jpeg)$", field_name: "обложка");
                _cover_photo_path = value;
            }
        }

        public string LibraryLocation
        {
            get { return _library_location; }
            set 
            {
                FieldValidator.Validate(value, field_name: "расположение");
                _library_location = value;
            }
        }

        public Book(ushort id, string title, string isbn, ushort total_pages, ushort amount, ushort publication_year, ushort publisher_id, decimal price, string annotation, string cover_photo_path = "../TableData/BooksPhoto/default_book_cover.png", string library_location = null)
        {
            ID = id;
            Title = title;
            ISBN = isbn;
            TotalPages = total_pages;
            Amount = amount;
            PublicationYear = publication_year;
            PublisherID = publisher_id;
            Price = price;
            Annotation = annotation;
            CoverPhotoPath = cover_photo_path;
            LibraryLocation = library_location;
        }
    }
}