pragma solidity ^0.4.0;

contract SummerForgotten {

		string public description;

		address owner;
		uint constant percentage = 0.3 ether;
		mapping (address => uint) public purchasers;

		function SummerForgotten(string _description) {
				owner = msg.sender;

				description = _description;
		}

		function transfer(uint totalIncome) payable {
				if (msg.value < (totalIncome * percentage)) {
						throw;
				}

				purchasers[msg.sender] += totalIncome;

		}

}
