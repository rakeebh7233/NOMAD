import React from "react";
import Select from 'react-select';
import axios from "axios";
import "../styles/Home.css"
import { useEffect, useState } from "react"; 
import { useParams } from "react-router-dom";

function Home(){
    return(
        <div>            
            {/* <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
            <header class="mb-auto">
                <div>
                <h3 class="float-md-start mb-0">Cover</h3>
                <nav class="nav nav-masthead justify-content-center float-md-end">
                    <a class="nav-link fw-bold py-1 px-0 active" aria-current="page" href="#">Home</a>
                    <a class="nav-link fw-bold py-1 px-0" href="#">Features</a>
                    <a class="nav-link fw-bold py-1 px-0" href="#">Contact</a>
                </nav>
                </div>
            </header> */}

            <main class="px-3">
                <h1>Welcome to NOMAD</h1>
                <p class="lead">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed id sagittis justo. Nam at lorem vel arcu hendrerit mattis quis sit amet sapien. Quisque enim ipsum, scelerisque vitae rutrum sit amet, fermentum non sem. Suspendisse potenti. Nunc feugiat felis nec enim ultrices semper.</p>
                <p class="lead">
                <a href="#" class="btn btn-lg btn-light fw-bold border-white bg-white">Learn more</a>
                </p>
            </main>

            <footer class="mt-auto text-white-50">
                <p>NOMAD</p>
            </footer>
        </div>
    );
}

export default Home