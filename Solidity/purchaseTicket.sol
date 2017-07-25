pragma solidity ^0.4.0;

contract FuncConcert {

		string public description;

		address owner;
		uint tickets;
		uint constant price = 1 ether;
		mapping (address => uint) public purchasers;

		function FuncConcert(string _description) {
				owner = msg.sender;
				tickets = 5;

				description = _description;
		}

		function buyTickets(
			  uint amount) payable {
				if (msg.value != (amount * price) || amount > tickets) {
						throw;
				}



				purchasers[msg.sender] += amount;
				tickets -= amount;


		}


}
