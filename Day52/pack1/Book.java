package pack1;

public class Book {
	int bookid;
    String title;
    Author author;
	public Book(int bookid, String title, Author author) {
		super();
		this.bookid = bookid;
		this.title = title;
		this.author = author;
	}
	public Book(int bookid, String title) {
		super();
		this.bookid = bookid;
		this.author = author;
	}
	
	public void setAuthor(Author author) {
		this.author = author;
	}
	
	

}
