`timescale 1ns/1ns

// Testing IR

module ir_test ();

	reg CLK;
	reg FETCH;
	wire PHI1;
	wire PHI2;

	always #1 CLK = ~CLK;

	ClkGen clk (.PHI0(CLK), .PHI1(PHI1), .PHI2(PHI2));

	IR ir (
		.PHI1(PHI1), .PHI2(PHI2),
		.n_PD(8'ha5), .FETCH(FETCH) );

	initial begin

		$dumpfile("ir_test.vcd");
		$dumpvars(0, ir_test);

		CLK <= 1'b0;
		FETCH <= 1'b0;

		repeat (8) @ (posedge CLK);

		FETCH <= 1'b1;
		repeat (8) @ (posedge CLK);

		FETCH <= 1'b0;
		repeat (8) @ (posedge CLK);

		$finish;
	end

endmodule // ir_test
