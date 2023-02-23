import React, { useState, useEffect } from 'react';

export default function Snapshots() {
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
                    <p className="logs">key={i}   {member[1]} {member[2]}</p> 
                ))
            )
            }
        </div>
    )
}