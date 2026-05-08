class students {
    public int id { get, set },
    public varchar name { get, set },
    public int salary { get, set },
    public int managerID { get, set }; 



public students () { }

public students(int id, varchar, name, int, salary. int managerID)
{

        id = id;
        name = name;
        salary = salary;
        managerID = managerID;

}

public striing Obtener resultado()
    {  return $"{id}, [managerID]"
}
