
// proxy space initialization
s.reboot;
p = ProxySpace.push(s.boot);
p.fadeTime = 5;
s.meter;


(
// allocating sample buffer
s.sendMsg(\b_allocRead, 10, "/Users/marnin/Desktop/hackathon/resources/whisper_swedish.wav");


// OSC responder for setting parameters
OSCdef(\params,
	{|msg|
		msg.postln;

		case
		{msg[1].asInteger == 0}{~zero.xset(\vol, msg[2].asFloat.clip(0, 1), \freq, msg[3].asFloat.linlin(0, 1, 0, 10), \range, msg[4].asFloat.linlin(0, 1, 0, 50))}
		{msg[1].asInteger == 1}{~one.xset(\vol, msg[2].asFloat.clip(0, 1), \freq, msg[3].asFloat.linlin(0, 1, 0, 10), \range, msg[4].asFloat.linlin(0, 1, 0, 50))}
		{msg[1].asInteger == 2}{~two.xset(\vol, msg[2].asFloat.clip(0, 1), \freq, msg[3].asFloat.linlin(0, 1, 0, 10), \range, msg[4].asFloat.linlin(0, 1, 0, 50))}
		{msg[1].asInteger == 3}{~three.xset(\vol, msg[2].asFloat.clip(0, 1), \freq, msg[3].asFloat.linlin(0, 1, 0, 10), \range, msg[4].asFloat.linlin(0, 1, 0, 50))}
		{msg[1].asInteger == 4}{~four.xset(\vol, msg[2].asFloat.clip(0, 1), \freq, msg[3].asFloat.linlin(0, 1, 0, 10), \range, msg[4].asFloat.linlin(0, 1, 0, 50))}
		{msg[1].asInteger == 5}{~five.xset(\vol, msg[2].asFloat.clip(0, 1), \freq, msg[3].asFloat.linlin(0, 1, 0, 10), \range, msg[4].asFloat.linlin(0, 1, 0, 50))}
		{msg[1].asInteger == 6}{~six.xset(\vol, msg[2].asFloat.clip(0, 1), \freq, msg[3].asFloat.linlin(0, 1, 0, 10), \range, msg[4].asFloat.linlin(0, 1, 0, 50))}
	},
	'/params', recvPort:50000);


///////////// set up sound environment

// reset layers
~zero.clear; ~one.clear; ~two.clear; ~three.clear; ~four.clear; ~five.clear; ~six.clear;


// layer 0
~zero = {|vol=0, freq=0, range=0| SinOsc.ar(200+SinOsc.kr(freq, 0, range))!2 * vol};

~zero.play;

// layer 1
~one = {|vol=0, freq=0, range=0| SinOsc.ar(420.43+SinOsc.kr(freq, 0, range))!2 * vol};

~one.play;

// layer 2
~two = {|vol=0, freq=0, range=0| SinOsc.ar(572+SinOsc.kr(freq, 0, range))!2 * vol};

~two.play;

// layer 3
~three = {|vol=0, freq=0, range=0| Saw.ar(633+SinOsc.kr(freq, 0, range))!2 * vol};

~three.play;

// layer 4
~four = {|vol=0, freq=0, range=0| SinOsc.ar(865+SinOsc.kr(freq, 0, range))!2 * vol};

~four.play;

// layer 5
~five = {|vol=0, freq=0, range=0| SinOsc.ar(1010+SinOsc.kr(freq, 0, range))!2 * vol};

~five.play;

// layer 6
~six = {|vol=0, freq=0, range=0| Saw.ar(1385.4+SinOsc.kr(freq, 0, range))!2 * vol};

~six.play;

p.fadeTime = 5;
)
(
m = NetAddr("127.0.0.1", 50000);

m.sendMsg('/params', 0, 1, 0, 0)

)


//////////////// workbench //////////////////////////////////////////////////////
// klankbell (bass version?), bassrumble, crackle, glitch, tube
// possible fx: filter, reverb, rhythm lfo

~bee = {~bee0 = LocalIn.ar(2);~bee1=LFSaw.ar(~bee0,0,~bee0,1);~bee2=~bee1.range(0.25,4.0);~bee3=PitchShift.ar(SinOscFB.ar(~bee2*20,~bee1),[0.05,0.03],~bee2);5.do{~bee3=~bee3.tanh+(~bee3*0.1)};LocalOut.ar(~bee3); Out.ar(0, ~bee0*0.7!2)}.play;

ProxySpace.pop
p = ProxySpace.push(s.boot);


(
s.sendMsg(\b_allocRead, 10, "/Users/marnin/Desktop/hackathon/resources/whisper_swedish.wav");
//b = Buffer.read(s, "/Users/marnin/Desktop/hackathon/resources/whisper_swedish.wav");


~tesst[0] = {
	var b = 10, trate, dur;

  trate = LFNoise0.kr(1).range(0.3, 1.0);
  dur = 1.9 / trate;
	TGrains.ar(2, Impulse.kr(trate), b,
    (1.2 ** WhiteNoise.kr(3).round(1)),
    LFNoise0.kr(5).range(0,BufDur.kr(b)),
    dur,
    WhiteNoise.kr(0.6), 0.1)*1;
};
//~tesst[10] = \filter -> {|in| in * 2}

)
~tesst.vol_(0)
~tesst.play
~tesst.clear
~tesst.play(fadeTime: 30)
~tesst.clear(120)


m = ProxyMixer(p);

s.meter

{PlayBuf.ar(2, bufnum: 10, rate: 1, trigger: 1, startPos: 0, loop: 0, doneAction: 0)}.play









