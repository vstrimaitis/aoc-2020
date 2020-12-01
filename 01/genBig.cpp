// #define INTERACTIVE
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
template <typename T> using min_heap = priority_queue<T, vector<T>, greater<T>>;
template <typename T> using max_heap = priority_queue<T, vector<T>, less<T>>;
 
template<typename A, typename B> ostream& operator<<(ostream& out, pair<A, B> p) { out << "(" << p.first << ", " << p.second << ")"; return out;}
template<typename T> ostream& operator<<(ostream& out, vector<T> v) { out << "["; for(auto& x : v) out << x << ", "; out << "]";return out;}
template<typename T> ostream& operator<<(ostream& out, deque<T> v) { out << "["; for(auto& x : v) out << x << ", "; out << "]";return out;}
template<typename T> ostream& operator<<(ostream& out, set<T> v) { out << "{"; for(auto& x : v) out << x << ", "; out << "}"; return out; }
template<typename K, typename V> ostream& operator<<(ostream& out, map<K, V> m) { out << "{"; for(auto& e : m) out << e.first << " -> " << e.second << ", "; out << "}"; return out; }
 
template<typename T> T read() {T x;cin >> x;return x;}
template<typename T> vector<T> read(int n) {vector<T> v(n);for(auto& x : v) cin >> x;return v;}
template<typename A, typename B>istream& operator>>(istream& in, pair<A, B>& p) {return in >> p.first >> p.second;}
template<class... Args> auto createVec(size_t n, Args&&... args) { if constexpr(sizeof...(args) == 1) return vector(n, args...); else return vector(n, create(args...)); }
 
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr)
#define TESTS(t) int NUMBER_OF_TESTS; cin >> NUMBER_OF_TESTS; for(int t = 1; t <= NUMBER_OF_TESTS; t++)
#define FOR(i, begin, end) for (int i = (begin); i < (end); i++)
#define sgn(a)     ((a) > eps ? 1 : ((a) < -eps ? -1 : 0))
#define precise(x) fixed << setprecision(x)
#define all(a) a.begin(), a.end()
#define pb push_back
#define rnd(a, b) (uniform_int_distribution<int>((a), (b))(rng))
#ifndef LOCAL
    #define cerr if(0)cout
    #ifndef INTERACTIVE
        #define endl "\n"
    #endif
    #define debug(args...) if(0){}
#else
    #define debug(args...) { string _s = #args; replace(_s.begin(), _s.end(), ',', ' '); stringstream _ss(_s); istream_iterator<string> _it(_ss); dbg(_it, true, args); }
    void dbg(istream_iterator<string> it, bool isStart) {cerr << "</debug>" << endl;}
    template<typename T, typename... Args>
    void dbg(istream_iterator<string> it, bool isStart, T a, Args... args) {
        if(isStart) cerr << "<debug>" << endl;
        cerr << "  " << *it << " = " << a << endl;
        dbg(++it, false, args...);
    }
#endif
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
std::chrono::steady_clock::time_point __clock__;
void startTime() {__clock__ = std::chrono::steady_clock::now();}
ld getTime() {
    auto end = std::chrono::steady_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::microseconds> (end-__clock__).count();
    return ld(t)/1e6;
}
void timeit(string msg) {
    cerr << "> " << msg << ": " << precise(6) << getTime() << endl;
}
template<typename T> inline bool maxi(T& a, T b) { return b > a ? (a = b, true) : false; }
template<typename T> inline bool mini(T& a, T b) { return b < a ? (a = b, true) : false; }
const ld PI = asin(1) * 2;
const ld eps = 1e-6;
const int oo = 2e9;
const ll OO = 2e18;
const ll MOD = 1000000007;
const int MAXN = 200000;
 
int main()
{
    FAST_IO;
    
    const int N = 100000;
    const int TUPLE_SIZE = 3;
    const int MIN = 1;
    const int MAX = 2020;
    const int SMALL_MAX = 500;
    const int SUM = 2020;

    vector<int> nums;
    FOR(_, 0, N-TUPLE_SIZE) {
        nums.pb(rnd(MIN, SMALL_MAX));
    }
    if (TUPLE_SIZE == 2) {
        const auto LIM = SUM - SMALL_MAX;
        auto x = rnd(SMALL_MAX, LIM+1);
        auto y = SUM - x;
        nums.pb(x);
        nums.pb(y);
    } else if (TUPLE_SIZE == 3) {
        vector<int> ints1;
        FOR(x, SMALL_MAX, MAX+1) ints1.pb(x);
        shuffle(all(ints1), rng);
        auto ints2 = ints1; shuffle(all(ints2), rng);
        auto ints3 = ints1; shuffle(all(ints3), rng);

        bool ok = false;
        for(auto x : ints1) {
            for(auto y : ints2) {
                for(auto z : ints3) {
                    if(ok) break;
                    if (x+y+z == SUM) {
                        ok = true;
                        nums.pb(x);
                        nums.pb(y);
                        nums.pb(z);
                    }
                }
            }
        }
    } else {
        cerr << "TUPLE_SIZE must be either 2 or 3" << endl;
        exit(1);
    }
    shuffle(all(nums), rng);

    for(auto x : nums) {
        cout << x << endl;
    }

}