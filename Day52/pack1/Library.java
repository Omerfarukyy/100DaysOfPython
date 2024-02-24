package pack1;

import java.util.ArrayList;

import javax.swing.JOptionPane;

public class Library {
	
	ArrayList<Author> authors = new ArrayList<Author>();
	
	
	public String getString(String message) {
		return JOptionPane.showInputDialog(message); 
	}
	
	public int getInt(String message) {
		return Integer.parseInt(JOptionPane.showInputDialog(message));
	}
	
	public void newAuthor() {
		Author auth = new Author(getInt("Author ID"),
								 getString("AuthorName"),
								 getString("Author Surname"));
		this.authors.add(auth);
		JOptionPane.showMessageDialog(null, "Author Saved!");
	}
	
	public void newBook(int authorId) {

		Book book = new Book(getInt("Book Id"), getString("Book title"));
		for (Author a : authors) {
			if(a.authorid == authorId) {
				a.addBook(book);
				book.setAuthor(a);
			}
		}
	
	}
	
	public void getAuthors() {
		String output = "";
		for (Author a : authors) {
			output +=a.authorid+" "+a.name+" "+a.surname+"\n";
			for (Book b: a.books) {
				output += b.bookid+" "+b.title+"/n";
			}
		}
		JOptionPane.showMessageDialog(null, output);
	}
	
	public void getAuthor(int AuthorId) {
		String output = "";
		
		for (Author a : authors) {
		
			if (a.authorid == AuthorId) {
			
				output +=a.authorid+" "+a.name+" "+a.surname+"\n";
				
				for (Book b: a.books) {
					output += b.bookid+" "+b.title+"/n";
				
				}
			}
			
		}
		JOptionPane.showMessageDialog(null, output);
	}
	
	public void getBooks() {
		
		String output = "";
		this.authors.forEach(a -> a.books.forEach(b -> System.out.println(b.title)));
		JOptionPane.showMessageDialog(null, output);
	}
	
	public void getBook(int AuthorId) {
		String output = "";
		this.authors.forEach(a -> a.books.forEach(b -> System.out.println(b.title)));
		JOptionPane.showMessageDialog(null, output);
		
		
		this.authors.stream().filter(a -> a.authorid==AuthorId).toList()
		.forEach(a -> a.books
		.forEach(b -> System.out.println()));
		
		this.authors.stream()
		.filter(a -> a.authorid== AuthorId)
		.findFirst()
		.get().books
		.forEach(b -> System.out.println(b.title));
		
	}
	
	
	public static void main(String[] args) {
		
		Library lib = new Library();
		
		lib.newAuthor();
		lib.newAuthor();
		
		lib.newBook(1);
		lib.newBook(2);
		
		lib.getAuthors();
		lib.getBooks();
		lib.getBook(1);
	}
}
