package creatingClass;

public class Dog {
    String dogType;
    String dogName;
    String dogColor;
    int dogAge;


    public void Dog(String dogType, String dogName,String dogColor,int dogage)
    {
        this.dogType = dogType;
        this.dogName = dogName;
        this.dogColor = dogColor;
        this.dogAge=dogage;

    }

    public void setDogType(String dogType)
    {
        this.dogType=dogType;
    }

    public String getDogType() {
        return dogType;
    }
    public void setDogName(String dogName)
    {
        this.dogName=dogName;
    }
    public String getDogName(){
        return dogName;
    }
    public void setDogColor(String dogColor)
    {
        this.dogColor=dogColor;
    }
    public String getDogColor()
    {
        return dogColor;
    }
    public void setDogAge(int dogage)
    {
        this.dogAge=dogage;
    }
    public int getDogAge()
    {
        return dogAge;
    }
    @Override
    public String toString() {
        return "Dog type:" + dogType + " Dog name:" + dogName + " Dog Color:" + dogColor + "  Dog age" + dogAge;
    }

    public class DogTester {

        public static void main(String[] args) {
            Dog bob = new Dog();

            System.out.println(bob);

        }
    }
}
