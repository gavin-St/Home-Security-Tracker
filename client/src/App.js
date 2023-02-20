import React, { useState, useEffect } from 'react';

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
                {(typeof data === 'undefined') ? (
                    <p>Loading...</p>
                ) : (
                    data.map((member,i) => (
                        <p>key={i}   {member[1]} {member[2]}</p> 
                    ))
                )
            
            }
            </div>
    )
}


export default App;