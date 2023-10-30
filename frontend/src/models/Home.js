import React from "react";
import Select from 'react-select';
import axios from "axios";
import "../styles/Home.css";
import { useEffect, useState } from "react"; 
import { useParams } from "react-router-dom";



function Home(){
    return(
        <div class="container">
            <div class="cover">
                <h1>Your Next Journey Awaits</h1>
                <form  class="flex-form">
                <label for="from">
                    <i class="ion-location"></i>
                </label>
                <input type="search" placeholder="Where do you want to go?"/>
                <input type="submit" value="Search"/>
                </form>
            </div>
        </div>
    );
}

export default Home