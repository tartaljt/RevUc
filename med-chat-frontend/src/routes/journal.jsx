import React, {useState, useEffect} from "react";
import * as io from 'socket.io-client';
import { Form } from "react-router-dom";

let endpoint = "http://localhost:5000";
//let socket = io.connect(`${endpoint}`);

export default function Chat() {
    //const [messages, setMessages] = useState([]);
    //const [message, setMessage] = useState("");
    const [userID, setUserID] = useState(-1);
    //const [toUserId, setToUserID] = useState(-1);
    //useEffect(() => {
    //    getMessages();
    //}, [message.length]);

    //const getMessages = () => {
    //    socket.on("message", (message) => {
    //        setMessages([...messages, message]);
    //    });
    //}

    //const onChange = (e) => {
    //    setMessage(e.target.value);
    //}

    //const sendMessage = () => {
    //    if(message !== "" && userID !== -1){
    //        //console.log("sending message:" + JSON.stringify({"fromUser": userID, "toUser": toUserId, "message": message}));
    //        socket.emit("message", JSON.stringify({"fromUser": userID, "toUser": toUserId, "message": message}));
    //        setMessage("");
    //    } else {
    //        alert("Please type a message");
    //    }
    //};

    const onUserIDChange = (e) => {
        setUserID(e.target.value);
    };
    //
    //const onToUserIDChange = (e) => {
    //    setToUserID(e.target.value);
    //};


    const sendJournal = () => {
        console.log(document.getElementById("freeform").value)
        fetch(endpoint + '/journal', {  // Enter your IP address here
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        mode: 'cors',
        contentType: 'application/json',
        body: JSON.stringify({'userID': userID, 'journal': document.getElementById("freeform").value})
        })
    };

  return (
    <div id="journal">
        <Form>
            <p>Enter your user ID</p>
            <input type="integer" placeholder="Enter a userID" value={userID} name = "id" onChange={e => onUserIDChange(e)} />
        </Form>
        <p>Journal</p>
        <textarea id="freeform" name="freeform" rows="6" cols="50">
    </textarea>
    <Form>
        <button type="submit" onClick={sendJournal}>Send</button>
    </Form>
    </div>
  );
}