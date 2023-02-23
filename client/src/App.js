import React, { useState, useEffect } from 'react';
import { NavBar } from "./components/NavBar";
import { Video } from "./components/Video";
import { SnapshotSubmit } from "./components/SnapshotSubmit";
import { Snapshots } from "./components/Snapshots";
import { Users } from "./components/Users";


function App() {
    const [data, setData] = useState([{}])

    useEffect(() => {
        fetch("/snapshots").then(
            res => res.json()
        ).then(
            data => {
                setData(data)
                console.log(data)
            }
        )
    }, [])

    return (
        <div>
            <NavBar />
            <Video />
            <SnapshotSubmit />
            <Snapshots />
            <Users />
                <div>
                    {(typeof data === 'undefined') ? (
                        <p>Loading...</p>
                    ) : (
                        data.map((member,i) => (
                            <p>key={i}   {member[1]} {member[2]}</p> 
                        ))
                    )
                
                }
                </div>
        </div>
    )
}


export default App;