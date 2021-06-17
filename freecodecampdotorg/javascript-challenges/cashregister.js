function checkCashRegister(price, cash, cid) {
    let difference = cash - price;
    let dinoms = {
        "PENNY": 0.01,
        "NICKEL": 0.05,
        "DIME": 0.10,
        "QUATER": 0.25,
        "ONE": 1.00,
        "FIVE": 5.00,
        "TEN": 10.00,
        "TWENTY": 20.00,
        "ONE HUNDRED": 100.00
    }
    let totalCash = 0;
    for (let i = 0; i < cid.length; i++) {
        totalCash += cid[i][1];
    }
    let cashRegister = {
        status: "CLOSED",
        change: []
    }

    // HANDLE INSUFFICIENT FUNDS
    if (difference > totalCash) {
        cashRegister.status = "INSUFFICIENT_FUNDS" ; 
    };

    // HANDLE EXACT CHANGE
    if (difference == 0) {
        cashRegister.change = cid;
    }

    console.log(difference);

    if (difference >= 100) {
        if (cid[8][1] <= difference) {
            difference -= 100;
            change = change.push
        }

    }

    console.log(cashRegister);


    // check if sufficient funds

    return cashRegister;
  }
  
  checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);