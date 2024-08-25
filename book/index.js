import axios from "axios";
import pg from "pg";
import express from "express";
import bodyParser from "body-parser";

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true}));
app.use(express.static("public"));

let currentUser = 0;
let users = [];

const db = new pg.Client({
    user: "postgres",
    host: "localhost",
    database: "book",
    password: "12345",
    port: 5432
  });

  db.connect()

async function getUsers(){
    users = [];
    let use = await db.query("SELECT * FROM use");
    users = use.rows;
    
}
getUsers();

let use = db.query("SELECT * FROM use");
users = use.rows;

app.get("/", async(req, res) => {
    const response = await db.query("SELECT * FROM users");
    const result = response.rows;
    console.log(result);
    res.render("index.ejs", { user: result, number: currentUser, name: users })
});
  
app.get("/users", async(req, res) => {
    await getUsers();
    console.log(users.length);
    res.render("users.ejs", { user: users, tamanho: users.length });
});

app.post("/users", (req, res) => {
    currentUser = parseInt(Object.keys(req.body)[0]) - 1;
    console.log(currentUser);
});

app.get("/new", (req, res) => {
    res.render("newPost.ejs");
});

app.post("/new", async(req, res) => {
    const titulo = req.body["lName"];
    const conteudo = req.body["content"];
    nameBook = titulo.replace(/ /g, '+');
    console.log(nameBook);
    try{
        const response = await axios.get("https://openlibrary.org/search.json?title=" + nameBook);
        const result = response.data.docs[0].cover_i;
        const responsta = "https://covers.openlibrary.org/b/id/" + result + "-S.jpg";
        console.log(responsta);
        await db.query("INSERT INTO users (conteudo, titulo, user_id, imagem) VALUES ($1, $2, $3, $4)", [conteudo, titulo, currentUser, responsta]);
        res.redirect("/");
    } catch (err){
        console.log(err);
        res.redirect("/");
    }
    
});


app.listen(port, () => {
    console.log("ta funfando")
});