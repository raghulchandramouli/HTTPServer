const express = require('express');
const app = express();

const users = [{
    name: 'John',
    kidneys: [{
        healthy: false,
    }]
}];

// GET request to retrieve kidney information for John
// Really popular `Query-Parameter`
app.get("/", function(req, res){
    const johnKidneys = users[0].kidneys;
    const numberOfKidneys = johnKidneys.length;
    let numberOfHealthyKidneys = 0;

    // healthy kidneys
    for (let i = 0; i < numberOfKidneys; i++) {
        if (johnKidneys[i].healthy) {
            numberOfHealthyKidneys++;
        }
    }

    const numberOfUnHealthyKidneys = numberOfKidneys - numberOfHealthyKidneys;
    res.json({
        numberOfKidneys,
        numberOfHealthyKidneys,
        numberOfUnHealthyKidneys
    })
});


// POST request to add a new kidney for John
// Send request in `Body`
app.post("/", function(req, res) {
    const isHealthy = req.body.isHealthy;
    users[0].kidneys.push({ 
             healthy: isHealthy
            });

    res.json({
        msg: "New kidney added successfully"
    })
});

app.listen(3000);