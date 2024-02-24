package pack1;

import java.util.ArrayList;
import java.util.List;

public class Author {
	     int authorid;
	     String name,surname;

	     ArrayList <Book> books = new ArrayList<Book>();
	    public Author(int authorid, String name, String surname) {
	        this.authorid = authorid;
	        this.name = name;
	        this.surname = surname;
	    }
	    public void addBook(Book b) {
	        this.books.add(b);
	        
	    }
}
