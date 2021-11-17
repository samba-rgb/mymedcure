const express = require("express");
const ejs = require("ejs");
const app = express();
const path = require("path");
const { title } = require("process");
const createCsvWriter = require("csv-writer").createObjectCsvWriter;

const multer = require("multer");
const cors = require("cors");
const port = process.env.PORT || 8080;

app.use(express.static(__dirname+"/public"))
   .use(express.json())
   .use(express.urlencoded({ extended: true
   }));
app.use(cors());

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));
app.use(express.static(path.join(__dirname, "public")));
// settinf csv for medicine adding
const csvWriter2 = createCsvWriter({
  path: path.join(__dirname, "/public/data.csv"),
  header: [
    // Title of the columns (column_names)
    { id: "medicine_name", title: "NAME" },
    { id: "link_of_medicine", title: "LINK" },
    { id: "information", title: "INFO" },
    {id : "count",title:"count"},
    {id:"expiry",title:"expiry"},
    { id: "monday", title: "monday" },
    {id:"monday_morning",title:"monday_morning"},
    {id:"monday_afternoon",title:"monday_afternoon"},
    {id:"monday_evening",title:"monday_evening"},
    {id:"monday_night",title:"monday_night"},
    { id: "tuesday", title: "tuesday" },
    {id:"tuesday_morning",title:"tuesday_morning"},
    {id:"tuesday_afternoon",title:"tuesday_afternoon"},
    {id:"tuesday_evening",title:"tuesday_evening"},
    {id:"tuesday_night",title:"tuesday_night"},
    { id: "wednessday", title: "wednessday" },
    {id:"wednessday_morning",title:"wednessday_morning"},
    {id:"wednessday_afternoon",title:"wednessday_afternoon"},
    {id:"wednessday_evening",title:"wednessday_evening"},
    {id:"wednessday_night",title:"wednessday_night"},
    { id: "thursday", title: "thursday" },
    {id:"thursday_morning",title:"thursday_morning"},
    {id:"thursday_afternoon",title:"thursday_afternoon"},
    {id:"thursday_evening",title:"thursday_evening"},
    {id:"thursday_night",title:"thursday_night"},
    { id: "friday", title: "friday" },
    {id:"friday_morning",title:"friday_morning"},
    {id:"friday_afternoon",title:"friday_afternoon"},
    {id:"friday_evening",title:"friday_evening"},
    {id:"friday_night",title:"friday_night"},
    { id: "saturday", title: "saturday" },
    {id:"saturday_morning",title:"saturday_morning"},
    {id:"saturday_afternoon",title:"saturday_afternoon"},
    {id:"saturday_evening",title:"saturday_evening"},
    {id:"saturday_night",title:"saturday_night"},
    { id: "sunday", title: "sunday" },
    {id:"sunday_morning",title:"sunday_morning"},
    {id:"sunday_afternoon",title:"sunday_afternoon"},
    {id:"sunday_evening",title:"sunday_evening"},
    {id:"sunday_night",title:"sunday_night"}
  ],
});

const fileStorageEngine = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, "./public"); //important this is a direct path fron our current file to storage location
  },
  filename: (req, file, cb) => {
    cb(null, "samba.csv");
    console.log( file.originalname);
  },
});

//setting up CSV writer for medical obervation
const csvWriter = createCsvWriter({
    path: path.join(__dirname, "/public/data_med.csv"),
    header: [
        { id: "medical_visit_name", title: "NAME" },
        {id:"Doctor_name",title: "Doctor name"},
        {id :"observation",title:"observation"},
        {id:"is_virtual",title:"is_virtual"},
        {id:"bp",title:"bp"},
        {id:"hemoglobin",title:"hemoglobin"},
        {id:"cell_count",title:"cell_count"}
      // Title of the columns (column_names)
      
    ],
  });


//homepage route
app.get("/", (req, res) => {
  res.render("main.ejs");
});

app.get("/api", (req, res) => {
  res.render("index.ejs");
});

app.get("/api2", (req, res) => {
  res.render("med_index.ejs");
});
app.get("/api3", (req, res) => {
  res.render("trail.ejs");
});

//submit page route
app.post("/api/add_medhis", (req, res) => {

  const {medical_visit_name,Doctor_name,observation,is_virtual,bp,hemoglobin,cell_count} = req.body
  // Values for each column through an array
  const results = [
    {medical_visit_name:medical_visit_name,
        Doctor_name:Doctor_name,
        observation:observation,
        is_virtual:is_virtual,
        bp:bp,
        hemoglobin:hemoglobin,
        cell_count:cell_count
     
    }
  ];
  csvWriter.writeRecords(results).then(() => {
    res.download(path.join(__dirname, "/public/data_med.csv"));
   
   
  });
});


const upload = multer({ storage: fileStorageEngine });

// Single File Route Handler
app.post("/single", upload.single("image"), (req, res) => {
  console.log(req.file);
  const csvtojson = require('csvtojson')
const fs = require('fs')

const csvfilepath = "./public/samba.csv"
csvtojson()
.fromFile(csvfilepath)
.then((json) => {
    console.log(json)

    fs.writeFileSync("./public/user.json",JSON.stringify(json),"utf-8",(err) => {
        if(err) console.log(err)
    })
})

  res.redirect('/api3')
});
app.post('/api/hi', (req,res)=>{
    res.download(path.join(__dirname, "/public/data_med.csv"));
})

app.post("/api/add_medicine", (req, res) => {

  const {medincine_name, link_of_medicine, information,count,expiry,monday,monday_morning,monday_afternoon,monday_evening,monday_night,tuesday,tuesday_morning,tuesday_afternoon,tuesday_evening,tuesday_night,wednessday,wednessday_morning,wednessday_afternoon,wednessday_evening,wednessday_night,thursday,thursday_morning,thursday_afternoon,thursday_evening,thursday_night,friday,friday_morning,friday_afternoon,friday_evening,friday_night,saturday,saturday_morning,saturday_afternoon,saturday_evening,saturday_night,sunday,sunday_morning,sunday_afternoon,sunday_evening,sunday_night} = req.body
  // Values for each column through an array
  const results = [
    {
      medicine_name: medincine_name,
      link_of_medicine: link_of_medicine,
      information: information,
      count:count,
      expiry:expiry,
      monday:monday.length-1,
      monday_morning:monday_morning.length -1,
      monday_afternoon:monday_afternoon.length-1,
      monday_evening:monday_evening.length-1,
      monday_night:monday_night.length-1,
      tuesday:tuesday.length-1,
      tuesday_morning:tuesday_morning.length-1,
      tuesday_afternoon:tuesday_afternoon.length-1,
      tuesday_evening:tuesday_evening.length-1,
      tuesday_night:tuesday_night.length-1,
      wednessday:wednessday.length-1,
      wednessday_morning:wednessday_morning.length-1,
      wednessday_afternoon:wednessday_afternoon.length-1,
      wednessday_evening:wednessday_evening.length-1,
      wednessday_night:wednessday_night.length-1,
      thursday:thursday.length-1,
      thursday_morning:thursday_morning.length-1,
      thursday_afternoon:thursday_afternoon.length-1,
      thursday_evening:thursday_evening.length-1,
      thursday_night:thursday_night.length-1,
      
      friday:friday.length-1,
      friday_morning:friday_morning.length-1,
      friday_afternoon:friday_afternoon.length-1,
      friday_evening:friday_evening.length-1,
      friday_night:friday_night.length-1,
      saturday:saturday.length-1,
      saturday_morning:saturday_morning.length-1,
      saturday_afternoon:saturday_afternoon.length-1,
      saturday_evening:saturday_evening.length-1,
      saturday_night:saturday_night.length-1,
      sunday:sunday.length-1,
      sunday_morning:sunday_morning.length-1,
      sunday_afternoon:sunday_afternoon.length-1,
      sunday_evening:sunday_evening.length-1,
      sunday_night:sunday_night.length-1
      
      
    }
  ];
  csvWriter2.writeRecords(results).then(() => {
     res.redirect('/api')
  });
});

app.post('/api/downloadhis', (req,res)=>{
    res.download(path.join(__dirname, "/public/data.csv"));
})

app.listen(port, () => console.log(`Server listening on port ${port}`));
