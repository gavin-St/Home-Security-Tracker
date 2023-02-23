import React, { useState, useEffect } from 'react';
import { NavBar } from "./components/NavBar";
import { Video } from "./components/Video";
import { SnapshotSubmit } from "./components/SnapshotSubmit";
import { Snapshots } from "./components/Snapshots";
import { Users } from "./components/Users";


function App() {

    return (
        <div>
            <NavBar />
            <Video />
            <SnapshotSubmit />
            <Snapshots />
            <Users />
        </div>
    )
}


export default App;