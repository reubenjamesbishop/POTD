import React, { useState } from "react";
import "./home.css";

const Home = () => {
  const [board, setBoard] = useState([]);

  const fetchBoard = (e) => {
    // e.preventDefault();
    let month = document.getElementById("month").value;
    let day = document.getElementById("day").value;
    fetch("http://127.0.0.1:5000/?month=" + month + "&day=" + day)
      .then((response) => response.json())
      .then((data) => renderSolution(data["board"]));
  };

  const renderSolution = (data) => {
    var daforbidden_array = [6, 13, 46, 47, 48, 49];
    var index_count = 0;
    var colour_string = "";
    let temp = data;
    for (var i = 0; i < temp.length; i++) {
      for (var j = 0; j < temp[0].length; j++) {
        // console.log(document.getElementById(index_count));
        if (!daforbidden_array.includes(index_count)) {
          console.log(temp[i][j]);
          switch (temp[i][j]) {
            case "A":
              colour_string = "red";
              break;
            case "B":
              colour_string = "orange";
              break;
            case "C":
              colour_string = "yellow";
              break;
            case "D":
              colour_string = "green";
              break;
            case "E":
              colour_string = "blue";
              break;
            case "F":
              colour_string = "indigo";
              break;
            case "G":
              colour_string = "violet";
              break;
            case "H":
              colour_string = "cyan";
              break;
            case 1:
              colour_string = "white";
              break;
            case "1":
              colour_string = "white";
              break;

            default:
              console.log("Oh no... our code... its broken...");
          }
          document.getElementById(index_count).style.backgroundColor =
            colour_string;
        }
        index_count++;
      }
    }
    setBoard(data);
  };

  return (
    <div class="container">
      <h1>Puzzle of the Day Solver</h1>
      <div class="row">
        <div class="left col-4">
          <table>
            <tr>
              <td id="0">Jan</td>
              <td id="1">Feb</td>
              <td id="2">Mar</td>
              <td id="3">April</td>
              <td id="4">May</td>
              <td id="5">Jun</td>
              <td id="6" style={{ backgroundColor: "grey" }}></td>
            </tr>
            <tr>
              <td id="7">Jul</td>
              <td id="8">Aug</td>
              <td id="9">Sep</td>
              <td id="10">Oct</td>
              <td id="11">Nov</td>
              <td id="12">Dec</td>
              <td id="13" style={{ backgroundColor: "grey" }}></td>
            </tr>
            <tr>
              <td id="14">1</td>
              <td id="15">2</td>
              <td id="16">3</td>
              <td id="17">4</td>
              <td id="18">5</td>
              <td id="19">6</td>
              <td id="20">7</td>
            </tr>
            <tr>
              <td id="21">8</td>
              <td id="22">9</td>
              <td id="23">10</td>
              <td id="24">11</td>
              <td id="25">12</td>
              <td id="26">13</td>
              <td id="27">14</td>
            </tr>
            <tr>
              <td id="28">15</td>
              <td id="29">16</td>
              <td id="30">17</td>
              <td id="31">18</td>
              <td id="32">19</td>
              <td id="33">20</td>
              <td id="34">21</td>
            </tr>
            <tr>
              <td id="35">22</td>
              <td id="36">23</td>
              <td id="37">24</td>
              <td id="38">25</td>
              <td id="39">26</td>
              <td id="40">27</td>
              <td id="41">28</td>
            </tr>
            <tr>
              <td id="42">29</td>
              <td id="43">30</td>
              <td id="44">31</td>
              <td id="46" style={{ backgroundColor: "grey" }}></td>
              <td id="47" style={{ backgroundColor: "grey" }}></td>
              <td id="48" style={{ backgroundColor: "grey" }}></td>
              <td id="49" style={{ backgroundColor: "grey" }}></td>
            </tr>
          </table>
        </div>
        <div class="right col">
          <h3>Instructions</h3>
          <p>
            A very cool tool to automatically solve this sick dragon fjord
            puzzle a day thing very cool!
          </p>
          <div class="row date-row">
            <form class="form-inline">
              <div class="form-group mx-3">
                Day:
                <input
                  class=" mx-2 form-control"
                  id="day"
                  type="number"
                  min="1"
                  max="31"
                  defaultValue="1"
                ></input>
              </div>
              <div class="form-group">
                Month:
                <select class="mx-2 form-control" id="month">
                  <option value="1">Jan</option>
                  <option value="2">Feb</option>
                  <option value="3">Mar</option>
                  <option value="4">Apr</option>
                  <option value="5">May</option>
                  <option value="6">Jun</option>
                  <option value="7">Jul</option>
                  <option value="8">Aug</option>
                  <option value="9">Sep</option>
                  <option value="10">Oct</option>
                  <option value="11">Nov</option>
                  <option value="12">Dec</option>
                </select>
              </div>
            </form>
          </div>
          <div class="form-group">
            {/* <div class="slider-container">
              <label for="customRange1" class="form-label">
                Number of Pieces to Display:
              </label>
              <input type="range" class="form-range" id="customRange1" />
            </div> */}
            <div class="form-group button-row button-container">
              <button
                class="form-control btn btn-success"
                onClick={(e) => fetchBoard()}
              >
                Show
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
export default Home;
