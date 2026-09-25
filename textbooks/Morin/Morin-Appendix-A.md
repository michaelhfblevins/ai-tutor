# Appendix A Useful formulas

### A.1 Taylor series

The general form of a Taylor series is

$$f(x_0 + x) = f(x_0) + f'(x_0)x + \frac{f''(x_0)}{2!}x^2 + \frac{f'''(x_0)}{3!}x^3 + \dots, \quad (\text{A.1})$$

which can be verified by taking derivatives and then setting  $x = 0$ . For example, taking the first derivative and then setting  $x = 0$  yields  $f'(x_0)$  on the left, and also  $f'(x_0)$  on the right, because the first term is a constant and gives zero, the second term gives  $f'(x_0)$ , and all the rest of the terms give zero once we set  $x = 0$  because they all have at least one power of  $x$  left in them. Likewise, if we take the second derivative of each side and then set  $x = 0$ , we obtain  $f''(x_0)$  on both sides. And so on for all derivatives. Therefore, since the two functions on each side of the above equation are equal at  $x = 0$  and also have their  $n$ th derivatives equal at  $x = 0$  for all  $n$ , they must in fact be the same function (assuming that they're nicely behaved functions, which we generally assume in physics).

Some specific Taylor series that come up often are listed below. They are all derivable via Eq. (A.1), but sometimes there are quicker ways of obtaining them. For example, Eq. (A.3) is most easily obtained by taking the derivative of Eq. (A.2), which itself is simply the sum of a geometric series.

$$\frac{1}{1-x} = 1 + x + x^2 + x^3 + \dots \quad (\text{A.2})$$

$$\frac{1}{(1-x)^2} = 1 + 2x + 3x^2 + 4x^3 + \dots \quad (\text{A.3})$$

$$\ln(1-x) = -x - \frac{x^2}{2} - \frac{x^3}{3} - \dots \quad (\text{A.4})$$

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots \quad (\text{A.5})$$

$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots \quad (\text{A.6})$$

$$\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots \quad (\text{A.7})$$

$$\sqrt{1+x} = 1 + \frac{x}{2} - \frac{x^2}{8} + \dots \quad (\text{A.8})$$

$$\frac{1}{\sqrt{1+x}} = 1 - \frac{x}{2} + \frac{3x^2}{8} + \dots \quad (\text{A.9})$$

$$(1+x)^n = 1 + nx + \binom{n}{2}x^2 + \binom{n}{3}x^3 + \dots \quad (\text{A.10})$$

### A.2 Nice formulas

The first formula here can be quickly proved by showing that the Taylor series for both sides are equal.

$$e^{i\theta} = \cos \theta + i \sin \theta \quad (\text{A.11})$$

$$\cos \theta = \frac{1}{2}(e^{i\theta} + e^{-i\theta}), \quad \sin \theta = \frac{1}{2i}(e^{i\theta} - e^{-i\theta}) \quad (\text{A.12})$$

$$\cos \frac{\theta}{2} = \pm \sqrt{\frac{1 + \cos \theta}{2}}, \quad \sin \frac{\theta}{2} = \pm \sqrt{\frac{1 - \cos \theta}{2}} \quad (\text{A.13})$$

$$\tan \frac{\theta}{2} = \pm \sqrt{\frac{1 - \cos \theta}{1 + \cos \theta}} = \frac{1 - \cos \theta}{\sin \theta} = \frac{\sin \theta}{1 + \cos \theta} \quad (\text{A.14})$$

$$\sin 2\theta = 2 \sin \theta \cos \theta, \quad \cos 2\theta = \cos^2 \theta - \sin^2 \theta \quad (\text{A.15})$$

$$\sin(\alpha + \beta) = \sin \alpha \cos \beta + \cos \alpha \sin \beta \quad (\text{A.16})$$

$$\cos(\alpha + \beta) = \cos \alpha \cos \beta - \sin \alpha \sin \beta \quad (\text{A.17})$$

$$\tan(\alpha + \beta) = \frac{\tan \alpha + \tan \beta}{1 - \tan \alpha \tan \beta} \quad (\text{A.18})$$

$$\cosh x = \frac{1}{2}(e^x + e^{-x}), \quad \sinh x = \frac{1}{2}(e^x - e^{-x}) \quad (\text{A.19})$$

$$\cosh^2 x - \sinh^2 x = 1 \quad (\text{A.20})$$

$$\frac{d}{dx} \cosh x = \sinh x, \quad \frac{d}{dx} \sinh x = \cosh x \quad (\text{A.21})$$

### A.3 Integrals

$$\int \ln x \, dx = x \ln x - x \quad (\text{A.22})$$

$$\int x \ln x \, dx = \frac{x^2}{2} \ln x - \frac{x^2}{4} \quad (\text{A.23})$$

$$\int x e^x \, dx = e^x(x - 1) \quad (\text{A.24})$$

$$\int \frac{dx}{1+x^2} = \tan^{-1}x \quad \text{or} \quad -\cot^{-1}x \quad (\text{A.25})$$

$$\int \frac{dx}{x(1+x^2)} = \frac{1}{2} \ln\left(\frac{x^2}{1+x^2}\right) \quad (\text{A.26})$$

$$\int \frac{dx}{1-x^2} = \frac{1}{2} \ln\left(\frac{1+x}{1-x}\right) \quad \text{or} \quad \tanh^{-1}x \quad (x^2 < 1) \quad (\text{A.27})$$

$$\int \frac{dx}{1-x^2} = \frac{1}{2} \ln\left(\frac{x+1}{x-1}\right) \quad \text{or} \quad \coth^{-1}x \quad (x^2 > 1) \quad (\text{A.28})$$

$$\int \sqrt{1+x^2} \, dx = \frac{1}{2} \left( x\sqrt{1+x^2} + \ln(x + \sqrt{1+x^2}) \right) \quad (\text{A.29})$$

$$\int \frac{1+x}{\sqrt{1-x}} \, dx = -\frac{2}{3}(5+x)\sqrt{1-x} \quad (\text{A.30})$$

$$\int \frac{dx}{\sqrt{1-x^2}} = \sin^{-1}x \quad \text{or} \quad -\cos^{-1}x \quad (\text{A.31})$$

$$\int \frac{dx}{\sqrt{x^2 + 1}} = \ln(x + \sqrt{x^2 + 1}) \quad \text{or} \quad \sinh^{-1} x \quad (\text{A.32})$$

$$\int \frac{dx}{\sqrt{x^2 - 1}} = \ln(x + \sqrt{x^2 - 1}) \quad \text{or} \quad \cosh^{-1} x \quad (\text{A.33})$$

$$\int \frac{dx}{x\sqrt{x^2 - 1}} = \sec^{-1} x \quad \text{or} \quad -\csc^{-1} x \quad (\text{A.34})$$

$$\int \frac{dx}{x\sqrt{1 + x^2}} = -\ln\left(\frac{1 + \sqrt{1 + x^2}}{x}\right) \quad \text{or} \quad -\text{csch}^{-1} x \quad (\text{A.35})$$

$$\int \frac{dx}{x\sqrt{1 - x^2}} = -\ln\left(\frac{1 + \sqrt{1 - x^2}}{x}\right) \quad \text{or} \quad -\text{sech}^{-1} x \quad (\text{A.36})$$

$$\int \frac{dx}{\cos x} = \ln\left(\frac{1 + \sin x}{\cos x}\right) \quad (\text{A.37})$$

$$\int \frac{dx}{\sin x} = \ln\left(\frac{1 - \cos x}{\sin x}\right) \quad (\text{A.38})$$

$$\int \frac{d\theta}{\sin \theta \cos \theta} = -\ln\left(\frac{\cos \theta}{\sin \theta}\right) \quad (\text{A.39})$$