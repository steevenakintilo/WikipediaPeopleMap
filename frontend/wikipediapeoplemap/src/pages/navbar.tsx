// import './global.css'
// import React, { useRef } from 'react';
// import { useNavigate } from 'react-router-dom';
// import { useState , useEffect } from 'react';
// import { Link } from "react-router-dom";
// import { polyfillCountryFlagEmojis } from "country-flag-emoji-polyfill";

// import { ToastContainer, toast } from 'react-toastify';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import './navbar.css'


export default function Custom_navbar(type:number = 0 , variable:any = "") {
    
    if (type === 0 ) {
        return (
        <nav className="navbar navbar-expand-lg  navbarBGcolor fixed-top navbar_color">
        <div className="container-fluid">
            
            <div className="d-grid gap-2">
                <a type="button" className="btn btn-dark" href="/Home" style={{margin :"auto"}}>Retourner au menu</a>
            </div>
            
            <select className="form-select" aria-label="Default select example">
                <option selected>Open this select menu</option>
                <option value="1">One</option>
                <option value="2">Two</option>
                <option value="3">Three</option>
            </select>
            
        </div>
        </nav>
    ) } else if (type === 2) {
        return (
        <nav className="navbar navbar-expand-lg  navbarBGcolor fixed-top navbar_color">
        <div className="container-fluid">
            <a className="navbar-brand navbar_text_color" href="/">LinkedinApplicationRecap</a>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
                <li className="nav-item">
                {/* <a className="navbar-brand navbar_text_color " aria-current="page" href="/" onClick={go_back_to_the_main_page()}>❌ Fermer</a> */}
                </li>
            </ul>
            </div>
        </div>
        </nav>
        )  
    }   
}
