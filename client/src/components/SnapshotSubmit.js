import React, { useState, useEffect } from 'react';

export default function SnapshotSubmit() {
    
    return (
        <div>   
            <form className="submit" action="/submit" method="POST"/>
                <label for="time">Time stamp:</label><br/>
                <input type="text" id="time" name="time"/><br/><br/>

                <label for="event">Event:</label><br/>
                <input type="text" id="event" name="event"/><br/><br/>

                <label for="trigger">Person(s) Recognized:</label><br/>
                <input type="text" id="trigger" name="trigger"/><br/><br/>

                <br/><br/>
                    <button><a>Send</a></button><br/>
        </div>
    )
}