#include <ranges>

class Solution {
public:
    string simplifyPath(string path) {
        vector<string> path_content;

        for (const auto& dir_view : views::split(path, '/')) {
            string dir = string(dir_view.begin(), dir_view.end());
            
            if (dir == "..") {
                if (path_content.size() > 0) {
                    path_content.pop_back();
                }
            } else if (!(dir == "" | dir == ".")) {
                path_content.push_back(dir);
            }
        }

        if (path_content.size() > 0) {
            string simplified_path;

            for (const auto& dir : path_content) {
                simplified_path.push_back('/');
                simplified_path.append(dir);
            }

            return simplified_path;
        } else {
            return "/";
        }
    }
};