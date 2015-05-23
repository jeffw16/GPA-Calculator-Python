/**
 * MyWikis
 * GPA Calculator (in Python, for CLI uses)
 * @author Jeffrey Wang
 * @contributors CJ Duffee
 * @license None
*/

class GPACalculator:
  dividend = 0.0;
  divisor = 0.0;
  quotient = 0.0;
  rawGrades = [];
  gpamax = [];
  
  def __init__ ( inRawGrades, inGPAMax):
    divisor = len(inRawGrades)-1
    rawGrades.extend( inRawGrades )
    gpamax.extend( inGPAMax )
  
  def calculateGPA ():
    for i in range ( 1, divisor ):
      pregrade = rawGrades[i]
      if pregrade > 100:
        pregrade = 100
      if pregrade < 0:
        pregrade = 0
      midgrade = pregrade - 60
  
  
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
