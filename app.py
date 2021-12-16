from flask import Flask, json, jsonify, request
from flask_cors import CORS
from POTD import *
app = Flask(__name__)
CORS(app)


@app.route("/")
def main():

    day = request.args.get('day')
    month = request.args.get('month')

    # day = 20
    # month = 6

    board = init_board([int(month), int(day)])

    solved = parallel_solve_puzzle(board)
    solved_dictionary = {'board': solved}
    return solved_dictionary


if __name__ == "__main__":
    app.run()
