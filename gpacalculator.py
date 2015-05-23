/**
 * MyWikis
 * GPA Calculator (in Python, for CLI uses)
 * @author Jeffrey Wang
 * @contributors CJ Duffee
 * @license None
*/

public class GPACalculator {
  // instance variables
  private double dividend = 0.0;
  private double divisor, quotient;
  private double[] rawGrades;
  private double[] gpamax;
  
  // constructors
  public GPACalculator ( double[] rawGrades, double[] gpamax ) {
    this.divisor = rawGrades.length-1;
    this.rawGrades = rawGrades;
    this.gpamax = gpamax;
  }
  /**public GPACalculator ( double[] rawGrades, int[] gpamax ) {
    this.dividend = dividend;
    this.divisor = divisor;
    this.gpamax = gpamax;
  }*/
  
  // mutator methods
  public void setRawGrade ( int pos, double rawGrade ) {
    if ( rawGrades.length >= pos && pos > 0 ) {
      this.rawGrades[pos] = rawGrade;
    }
  }
  public void setDivisor ( double divisor ) {
    this.divisor = divisor;
  }
  
  // accessor methods
  public double getRawGrade ( int pos ) {
    return rawGrades[pos];
  }
  public double getDivisor () {
    return divisor;
  }
  
  // methods
  public void calculateGPA () {
    // to be added soon
    for ( int i = 1; i <= divisor; i++ ) {
      double pregrade = rawGrades[i];
      if ( pregrade > 100 ) {
        System.out.println ( "Grades over 100 are set to 100 automatically." );
        pregrade = 100;
      }
      if ( pregrade < 0 ) {
        System.out.println ( "Grades less than 0 are set to 0 automatically." );
        pregrade = 0;
      }
      
      double midgrade = pregrade - 60;
      if ( midgrade < 0 ) {
        midgrade = 0;
      }
      
      double postgrade = midgrade / 10;
      postgrade += ( gpamax[i] - 4 );
      
      dividend += postgrade;
    }
    quotient = dividend / divisor;
  }
  
  public String toString() {
    return "" + quotient;
  }
  
  public static void main ( String[] args ) {
    Scanner s = new Scanner( System.in );
    System.out.println ( "GPA Calculator" );
    System.out.println ( "How many classes do you have?" );
    int classcount = s.nextInt();
    double[] grades = new double[classcount+1];
    double[] gpamax = new double[classcount+1];
    for ( int i = 1; i <= classcount; i++ ) {
      System.out.println ( "Grade for class " + i + ": " );
      grades[i] = s.nextDouble();
      System.out.println ( "GPA scale for class " + i + " (for example: 4, 5, or 6?): " );
      gpamax[i] = s.nextDouble();
    }
    GPACalculator g = new GPACalculator( grades, gpamax );
    g.calculateGPA();
    System.out.println ( "Your GPA is: " + g );
  }
}
