
import React from 'react';
import ReactPlayer from 'react-player';

export const Video = () => {
    
    const [camera, setCamera] = useState([{}])

    useEffect(() => {
        fetch("/cameras").then(
            res => res.json()
        ).then(
            camera => {
                setCamera(camera)
                console.log(camera)
            }
        )
    }, [])
    
    return (
    <div >       
        <ReactPlayer
                url=""
                width="100%"
                height="100%"
                controls
            />
            <div>
                {(typeof camera === 'undefined') ? (
                        <p>No Video feed detected</p>
                    ) : (
                            <p>Video feed from Camera #</p> 
                    )
                }
            </div>
    </div>
    )
}

